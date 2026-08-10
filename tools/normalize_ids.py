"""One-time id normalisation, with a permanent redirect map.

42 entities used Arabic digits where the convention calls for Roman regnal numerals --
`thutmose3`, `ramesses2`, `cleopatra7` -- and they sat alongside siblings that used Roman
ones. Thutmose I, II and IV lived at `thutmose-i`, `thutmose-ii`, `thutmose-iv` while Thutmose
III lived at `thutmose3`. An author reasoning from one sibling to another was right three
times in four, with no way to tell which time was the exception, and I guessed wrong on this
exact entity earlier in the project.

Every rename is recorded in `redirects`, written into the build output and resolved forever.
The map is not pruned: keeping an entry costs a line, and dropping one costs a link that
silently resolves to nothing.

Renaming an id means rewriting every reference to it, which is the part worth being careful
about -- `parent_id`, `cross_parent_ids`, `links[].entity_id`, and theme membership lists all
carry ids. The module rewrites references from the same map it publishes, so the two cannot
drift apart.
"""

import re

# Longest first, so XVIII is never matched as XV followed by stray letters.
ROMAN = [
    (30, "xxx"), (29, "xxix"), (28, "xxviii"), (27, "xxvii"), (26, "xxvi"), (25, "xxv"),
    (24, "xxiv"), (23, "xxiii"), (22, "xxii"), (21, "xxi"), (20, "xx"), (19, "xix"),
    (18, "xviii"), (17, "xvii"), (16, "xvi"), (15, "xv"), (14, "xiv"), (13, "xiii"),
    (12, "xii"), (11, "xi"), (10, "x"), (9, "ix"), (8, "viii"), (7, "vii"), (6, "vi"),
    (5, "v"), (4, "iv"), (3, "iii"), (2, "ii"), (1, "i"),
]
ARABIC_TO_ROMAN = dict(ROMAN)

# The display name must actually contain a Roman numeral for this to be a regnal number
# rather than, say, a site phase or a dynasty count.
_NAME_HAS_ROMAN = re.compile(r"\b(X{1,3}|IX|IV|V?I{1,3}|VI{0,3}|XI{1,2}|XV|XVI{1,3}|XX)\b")
_SLUG_TRAILING_DIGITS = re.compile(r"^(?P<stem>[a-z][a-z\-]*?)-?(?P<num>\d{1,2})$")


def _proposed(entity):
    """The convention-compliant slug for this entity, or None if it already complies."""
    # An event's numerals are dates, not regnal numbers. "September 11 Attacks" was rewritten to
    # `september-xi`, which is the same failure as `ww1` becoming `ww-i` -- and the guard added for
    # that one did not catch this, because here the slug stem genuinely IS the name's first word.
    # Kind is the discriminator that actually holds: rulers are counted, dates are not.
    if entity["kind"] == "event":
        return None
    slug = entity["id"].rsplit(".", 1)[-1]
    m = _SLUG_TRAILING_DIGITS.match(slug)
    if not m:
        return None
    # Requiring a Roman numeral in the display NAME was the first guard here and it was wrong
    # twice over. It could not match "XIV", so Louis XIV kept `louis14`. And it excluded rulers
    # whose display name is an epithet rather than a numeral -- William the Conqueror is
    # William I, Peter the Great is Peter I, and `william1` and `peter1` encode exactly the
    # regnal number the convention is about.
    #
    # The stem check below is the real discriminator, and it is sufficient on its own: a
    # regnal slug is built from the ruler's name, so the stem must BE that name. That excludes
    # `ww1` for "World War I", which is what the numeral guard was protecting against, because
    # "ww" is not "world".
    import unicodedata
    first = entity["name"].split()[0]
    folded = "".join(c for c in unicodedata.normalize("NFD", first)
                     if unicodedata.category(c) != "Mn").lower()
    folded = re.sub(r"[^a-z0-9]", "", folded)
    if folded != m.group("stem").replace("-", ""):
        return None
    numeral = ARABIC_TO_ROMAN.get(int(m.group("num")))
    if numeral is None:
        return None
    return f"{m.group('stem')}-{numeral}"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    # ---- plan the renames, refusing any that would collide -------------------
    renames = {}
    for e in entities:
        new_slug = _proposed(e)
        if new_slug is None:
            continue
        prefix = e["id"].rsplit(".", 1)[0]
        new_id = f"{prefix}.{new_slug}"
        if new_id == e["id"]:
            continue
        if new_id in by_id or new_id in renames.values():
            # Never silently merge two entities. If this fires the convention needs a
            # disambiguating qualifier for one of them, decided deliberately.
            raise ValueError(f"normalize_ids: {e['id']} -> {new_id} collides with an existing id")
        renames[e["id"]] = new_id

    if not renames:
        print("normalize_ids: nothing to rename")
        return

    # ---- apply to the entities themselves -----------------------------------
    for old, new in renames.items():
        by_id[old]["id"] = new

    # ---- rewrite every reference from the same map ---------------------------
    rewritten = 0
    for e in entities:
        if e.get("parent_id") in renames:
            e["parent_id"] = renames[e["parent_id"]]
            rewritten += 1
        if e.get("cross_parent_ids"):
            e["cross_parent_ids"] = [renames.get(i, i) for i in e["cross_parent_ids"]]
        for link in e.get("links") or []:
            if link.get("entity_id") in renames:
                link["entity_id"] = renames[link["entity_id"]]
                rewritten += 1

    print(f"normalize_ids: renamed {len(renames)} ids to Roman regnal numerals, "
          f"rewrote {rewritten} reference(s)")
    for old, new in list(renames.items())[:4]:
        print(f"  {old.rsplit('.', 1)[-1]} -> {new.rsplit('.', 1)[-1]}")

    return renames


def rewrite_refs(obj, renames):
    """Rewrite every entity id anywhere in a nested structure.

    Deliberately generic rather than per-file. The first attempt rewrote references inside the
    entity records and stopped there, which left nine dangling ids: themes carry membership
    lists and frames carry an `entity_id` each, and both broke silently the moment an id
    changed. Anything that holds an id needs to pass through the same map, so this walks the
    whole structure instead of enumerating the places I could think of.
    """
    if not renames:
        return 0
    count = 0

    def walk(node):
        nonlocal count
        if isinstance(node, dict):
            for k, v in node.items():
                if isinstance(v, str) and v in renames and (k == "entity_id" or k.endswith("_id")):
                    node[k] = renames[v]
                    count += 1
                elif isinstance(v, list) and k.endswith("_ids"):
                    for i, item in enumerate(v):
                        if isinstance(item, str) and item in renames:
                            v[i] = renames[item]
                            count += 1
                        else:
                            walk(item)
                else:
                    walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(obj)
    return count
