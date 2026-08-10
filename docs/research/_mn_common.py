ROWS = []
CFG = {"region": "global"}

def set_region(r):
    CFG["region"] = r

def E(slug, name, kind, start, end, extant, parent, summary, aliases=None, conf="high", region=None):
    ROWS.append({
        "suggested_id_slug": slug,
        "name": name,
        "kind": kind,
        "start_year": int(start),
        "end_year": (None if end is None else int(end)),
        "extant": bool(extant),
        "parent_hint": parent,
        "region_hint": region or CFG["region"],
        "start_dating_method": "calendar",
        "summary": " ".join(summary.split()),
        "aliases": aliases or [],
        "confidence": conf,
    })
    return ROWS[-1]
