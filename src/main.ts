import "./style.css";
import { datasetVersion, entities, sourceById } from "./dataset/dataset";
import { displayRange } from "./chrono/displayRange";
import { contextNeighbours } from "./focus/contextNeighbours";
import { datingOf } from "./chrono/fromEntity";
import { isCalendarConvertible } from "./chrono/year";
import {
  buildIndex,
  childrenOf,
  pathTo,
  searchEntities,
  visibleAtTier,
} from "./entity/tree";
import { formatYear } from "./entity/tree";
import type { CaveatKindId, Entity, EntityKind, StandingId, Tier } from "./entity/entity";
import type { Source } from "./dataset/dataset";
import { readYearIn, type CalendarReading } from "./calendars/convert";
import { CALENDARS, getCalendar } from "./calendars/registry";
import { parseSelection, serializeSelection, toggleCalendar } from "./calendars/selection";
import { asHistorical, isoFromHistorical } from "./chrono/year";
import { ambiguousNames, handoffTargets } from "./research/handoff";

const APP_VERSION = __APP_VERSION__;
const REPO_URL = "https://github.com/tyohDeveloper/history-and-prehistory";

const GLYPH: Record<EntityKind, string> = {
  region: "\u25A6",
  era: "\u25A3",
  period: "\u25C6",
  reign: "\u25CF",
  event: "\u25C7",
  taxon: "\u25D0",
  threshold: "\u25B3",
};

const STANDING_LABEL: Record<StandingId, string> = {
  consensus: "Consensus",
  majority: "Majority view",
  minority: "Minority view",
  // Kept distinct on purpose: a received date such as Rome's 753 BCE is not a
  // finding, and showing it with the same weight as a measured one is the
  // commonest way a history reference misleads.
  traditional: "Traditional date",
  superseded: "Superseded",
};

const SOURCE_KIND_LABEL: Record<Source["kind"], string> = {
  scholarly: "Peer-reviewed",
  institutional: "Institutional",
  reference: "Reference",
  news: "News",
};

const CAVEAT_LABEL: Record<CaveatKindId, string> = {
  misconception: "Common misconception",
  "naming-confusion": "Naming",
  "contested-existence": "Contested",
};

const KIND_LABEL: Record<EntityKind, string> = {
  region: "Region",
  era: "Era",
  period: "Period",
  reign: "Reign",
  event: "Event",
  taxon: "Species",
  threshold: "Earliest known",
};

const index = buildIndex(entities);

// Measured once over all 1,305 entities, not per render: ambiguity is a
// property of the dataset, and the dataset does not change at runtime.
const ambiguous = ambiguousNames(entities);

interface State {
  /** Selected node per column depth; index 0 is the root column. */
  path: string[];
  tier: Tier;
  query: string;
  /** Calendars shown in the readout. Persisted only in location.hash. */
  calendars: string[];
  calendarPickerOpen: boolean;
  /** Focus+context lens beside the columns. Q-9: a budget, not a tier filter. */
  contextOpen: boolean;
  contextBudget: number;
}

const state: State = {
  path: [],
  tier: "intermediate",
  query: "",
  calendars: parseSelection(window.location.hash),
  calendarPickerOpen: false,
  contextOpen: false,
  contextBudget: 24,
};

/**
 * Write the selection to the URL fragment without adding a history entry.
 * `replaceState` keeps the back button meaning "the page before this one"
 * rather than "the last calendar I ticked".
 */
function syncHash(): void {
  const next = serializeSelection(state.calendars);
  const url = window.location.pathname + window.location.search + next;
  window.history.replaceState(null, "", url);
}

const el = <K extends keyof HTMLElementTagNameMap>(
  tag: K,
  attrs: Record<string, string> = {},
  ...kids: (Node | string)[]
): HTMLElementTagNameMap[K] => {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
  for (const c of kids) n.append(c);
  return n;
};

function selected(): Entity | undefined {
  const last = state.path[state.path.length - 1];
  return last === undefined ? undefined : index.byId.get(last);
}

function selectEntity(id: string): void {
  state.query = "";
  state.path = pathTo(index, id).map((e) => e.id);
  render();
}

function selectAtDepth(depth: number, id: string): void {
  state.path = [...state.path.slice(0, depth), id];
  render();
}

function renderRow(e: Entity, depth: number, isSelected: boolean): HTMLElement {
  const row = el(
    "button",
    {
      class: "row",
      type: "button",
      role: "option",
      "aria-selected": String(isSelected),
      "data-testid": `option-tree-node-${e.id}`,
          title: `${KIND_LABEL[e.kind]} · ${displayRange(e).text}`,
    },
    el("span", { class: "glyph", "aria-hidden": "true" }, GLYPH[e.kind]),
    el("span", { class: "row-name" }, e.name),
    el("span", { class: "row-years" }, shortRange(e)),
  );
  row.addEventListener("click", () => selectAtDepth(depth, e.id));
  return row;
}

/**
 * Compact range for the narrow column gutter. The era marker is emitted
 * once, at the end, unless the range crosses the BCE/CE boundary:
 *   14000-300 BCE   |   300 BCE-300 CE   |   1603-1868   |   1868-
 * Magnitudes at or above a million are abbreviated (2.6M BCE) so the
 * Paleolithic does not blow out the column width.
 */
function magnitude(y: number): string {
  const a = Math.abs(y);
  if (a >= 1_000_000) return `${(a / 1_000_000).toFixed(1)}M`;
  if (a >= 100_000) return `${Math.round(a / 1000)}k`;
  return String(a);
}

function shortRange(e: Entity): string {
  const { start_year: s, end_year: t } = e;
  if (s === null) return "";
  const DASH = "\u2013";
  if (t === null) return `${magnitude(s)}${s < 0 ? "\u2009BCE" : ""}${DASH}`;
  if (s < 0 && t < 0) return `${magnitude(s)}${DASH}${magnitude(t)}\u2009BCE`;
  if (s < 0 && t >= 0) return `${magnitude(s)}\u2009BCE${DASH}${magnitude(t)}\u2009CE`;
  return `${magnitude(s)}${DASH}${magnitude(t)}`;
}

function renderColumns(): HTMLElement {
  const wrap = el("div", { class: "columns", "data-testid": "region-picker-columns" });

  if (state.query.trim().length > 0) {
    const hits = searchEntities(entities, state.query);
    const col = el("div", { class: "column", style: "flex-basis:340px" });
    col.append(
      el("div", { class: "column-head" }, `Search \u2014 ${hits.length} result${hits.length === 1 ? "" : "s"}`),
    );
    const body = el("div", { class: "column-body", role: "listbox", "data-testid": "list-search-results" });
    if (hits.length === 0) {
      body.append(el("div", { class: "empty" }, "No matches."));
    }
    for (const e of hits) {
      const row = renderRow(e, 0, false);
      row.addEventListener("click", (ev) => {
        ev.stopPropagation();
        selectEntity(e.id);
      });
      body.append(row);
    }
    col.append(body);
    wrap.append(col);
    return wrap;
  }

  // Column 0 is the root region list; each subsequent column is the
  // children of the node selected in the column before it.
  let parents: Entity[] = index.roots;
  let depth = 0;
  for (;;) {
    const visible = visibleAtTier(parents, state.tier);
    const heading =
      depth === 0
        ? "Regions"
        : (index.byId.get(state.path[depth - 1] ?? "")?.name ?? "");
    const col = el("div", { class: "column", "data-testid": `region-column-${depth}` });
    col.append(el("div", { class: "column-head" }, heading));
    const body = el("div", { class: "column-body", role: "listbox" });
    if (visible.length === 0) {
      body.append(el("div", { class: "empty" }, "No entries at this detail level."));
    }
    for (const e of visible) {
      body.append(renderRow(e, depth, state.path[depth] === e.id));
    }
    col.append(body);
    wrap.append(col);

    const chosen = state.path[depth];
    if (chosen === undefined) break;
    const next = childrenOf(index, chosen);
    if (next.length === 0) break;
    parents = next;
    depth += 1;
  }
  return wrap;
}

function renderReadout(): HTMLElement {
  const box = el("div", { class: "readout", "data-testid": "panel-readout-root" });
  const e = selected();
  if (!e) {
    box.append(
      el(
        "div",
        { class: "empty" },
        "Select a region to begin. Nothing you do here is saved \u2014 this app stores no data and makes no network requests.",
      ),
    );
    return box;
  }

  const trail = pathTo(index, e.id)
    .map((n) => n.name)
    .join(" \u203A ");
  box.append(el("div", { class: "breadcrumb", "data-testid": "text-readout-breadcrumb" }, trail));
  box.append(el("h2", { "data-testid": "text-readout-name" }, e.name));
  if (e.native_name !== undefined) {
    box.append(el("p", { class: "native", dir: "auto", "data-testid": "text-readout-native" }, e.native_name));
  }
    const range = displayRange(e);
  box.append(el("div", { class: "range", "data-testid": "text-readout-range" }, range.text));
  if (e.summary !== undefined) {
    box.append(el("p", { class: "summary" }, e.summary));
  }

  const dl = el("dl", { "data-testid": "list-readout-facts" });
  const fact = (k: string, v: string): void => {
    dl.append(el("dt", {}, k), el("dd", { dir: "auto" }, v));
  };
  fact("Kind", KIND_LABEL[e.kind]);
  fact("Detail tier", e.tier);
  fact("Identifier", e.id);
  if (e.date_precision !== undefined) fact("Date precision", e.date_precision);
  if (e.date_note !== undefined) {
    const dd = el("dd", { dir: "auto" }, e.date_note);
    const mark = citationMarker(e.source_ids, citationOrder(e));
    if (mark !== null) dd.append(" ", mark);
    dl.append(el("dt", {}, "Dating note"), dd);
  }
  if (e.aliases !== undefined && e.aliases.length > 0) fact("Also known as", e.aliases.join(", "));
  if (e.calendar_ids !== undefined && e.calendar_ids.length > 0) {
    fact("Calendars", e.calendar_ids.join(", "));
  }
  if (e.standing !== undefined) fact("Standing", STANDING_LABEL[e.standing]);
  if (e.capital !== undefined) fact("Capital", e.capital);
  if (e.as_of !== undefined) fact("Dispute last checked", e.as_of);
  box.append(dl);
  const order = citationOrder(e);
  const caveats = renderCaveats(e, order);
  if (caveats !== null) box.append(caveats);
  const alternatives = renderAlternatives(e, order);
  if (alternatives !== null) box.append(alternatives);
  const calendars = renderCalendarRows(e);
  if (calendars !== null) box.append(calendars);
  const sources = renderSources(order);
  if (sources !== null) box.append(sources);
  box.append(renderHandoff(e, order.length > 0));
  return box;
}

/**
 * The order citations are numbered in for one entity.
 *
 * Numbering is per-entity rather than global. A global scheme would give the
 * reader "[147]" on a panel showing three sources, which tells them nothing
 * and invites them to look for 146 others.
 *
 * Order follows the panel: the entity's own sources, then its caveats', then
 * its alternatives'. A source cited twice keeps its first number.
 */
function citationOrder(entity: Entity): string[] {
  const seen: string[] = [];
  const push = (ids: readonly string[] | undefined): void => {
    for (const id of ids ?? []) {
      // A dangling id would otherwise be numbered and then render as an empty
      // row in the source list, which reads as a missing citation rather than
      // as the data error it is.
      if (!seen.includes(id) && sourceById.has(id)) seen.push(id);
    }
  };
  push(entity.source_ids);
  for (const c of entity.caveats ?? []) push(c.source_ids);
  for (const a of entity.alternatives ?? []) push(a.source_ids);
  return seen;
}

/** `[1]`, `[2,3]` — or nothing, rather than an empty bracket. */
function citationMarker(ids: readonly string[] | undefined, order: string[]): HTMLElement | null {
  const ns = (ids ?? [])
    .map((id) => order.indexOf(id))
    .filter((i) => i >= 0)
    .map((i) => i + 1);
  if (ns.length === 0) return null;
  return el("sup", { class: "cite" }, `[${[...new Set(ns)].sort((a, b) => a - b).join(",")}]`);
}

/**
 * The sources themselves.
 *
 * Until 3.6.0.0 the readout showed none of these, and the handoff carried a
 * line saying the dates were "a starting point, not a citation" — accurate at
 * the time, and the reason a dataset with 175 cited entities read like an
 * uncited one.
 *
 * The URL is rendered as selectable text as well as a link, for the same
 * reason the research handoff does it: opened from a file:// path with no
 * network, the link goes nowhere and the reader's fallback is to write the
 * address down. ARCHITECTURE.md §10 permits exactly this — "named external
 * references cited in a readout" — and requires the link text be descriptive,
 * so the citation is the link and the bare URL is not.
 */
function renderSources(order: string[]): HTMLElement | null {
  if (order.length === 0) return null;
  const box = el("div", { class: "sources", "data-testid": "panel-sources-root" });
  box.append(el("div", { class: "sources-head" }, "Sources"));
  const list = el("ol", { class: "source-list" });
  for (const id of order) {
    const src = sourceById.get(id);
    if (src === undefined) continue;
    const li = el("li", { class: "source", "data-testid": `item-source-${id}` });
    if (src.url !== undefined) {
      li.append(
        el(
          "a",
          {
            class: "source-cite",
            href: src.url,
            target: "_blank",
            rel: "noopener noreferrer",
          },
          src.citation,
        ),
      );
    } else {
      li.append(el("span", { class: "source-cite", dir: "auto" }, src.citation));
    }
    li.append(el("span", { class: `source-kind source-${src.kind}` }, SOURCE_KIND_LABEL[src.kind]));
    if (src.url !== undefined) {
      li.append(el("code", { class: "source-url" }, src.url));
    }
    if (src.note !== undefined) {
      li.append(el("p", { class: "source-note", dir: "auto" }, src.note));
    }
    list.append(li);
  }
  box.append(list);
  return box;
}

/**
 * Caveats: the corrections the reader most likely needs.
 *
 * These were authored across several dataset passes and, until now, rendered
 * nowhere — 62 entities carried a `caveats` array that no code path read. The
 * dataset's whole reason for existing is that it says where the received story
 * is wrong, so leaving them unrendered removed the point of it.
 *
 * They sit above the calendar readout deliberately. A misconception about what
 * a date *means* is worth more than the same date expressed in four calendars.
 */
function renderCaveats(entity: Entity, order: string[]): HTMLElement | null {
  const items = entity.caveats ?? [];
  if (items.length === 0) return null;
  const box = el("div", { class: "caveats", "data-testid": "panel-caveats-root" });
  box.append(el("div", { class: "caveats-head" }, "Worth knowing"));
  const grid = el("div", { class: "caveat-grid" });
  for (const c of items) {
    grid.append(el("span", { class: `caveat-kind caveat-${c.kind}` }, CAVEAT_LABEL[c.kind]));
    const text = el("span", { class: "caveat-text", dir: "auto" }, c.text);
    const mark = citationMarker(c.source_ids, order);
    if (mark !== null) text.append(" ", mark);
    grid.append(text);
  }
  box.append(grid);
  return box;
}

/**
 * Rival dating claims, kept apart rather than averaged.
 *
 * A wide range implies the middle is likeliest. When the field actually
 * disagrees about which of two dates is right, that is a different claim, and
 * flattening it into one range misreports it — which is why `alternatives`
 * exists in the schema separately from the uncertainty bounds.
 *
 * The entity's own standing is shown alongside, so a `superseded` alternative
 * reads as history-of-the-field rather than as a live competitor.
 */
function renderAlternatives(entity: Entity, order: string[]): HTMLElement | null {
  const items = entity.alternatives ?? [];
  if (items.length === 0) return null;
  const box = el("div", { class: "alts", "data-testid": "panel-alternatives-root" });
  box.append(el("div", { class: "alts-head" }, "Competing dates"));
  for (const a of items) {
    const row = el("div", { class: "alt" });
    const head = el("div", { class: "alt-head" });
    head.append(el("span", { class: "alt-label", dir: "auto" }, a.label));
    head.append(el("span", { class: `alt-standing alt-${a.standing}` }, STANDING_LABEL[a.standing]));
    const mark = citationMarker(a.source_ids, order);
    if (mark !== null) head.append(mark);
    row.append(head);
    const span = altRange(a);
    if (span !== null) row.append(el("span", { class: "alt-range" }, span));
    if (a.note !== undefined) row.append(el("p", { class: "alt-note", dir: "auto" }, a.note));
    box.append(row);
  }
  return box;
}

/**
 * An alternative may carry no dates at all — Abbo and Gopher dispute the shape
 * of the Neolithic transition, not its calendar years — so the range is
 * omitted rather than rendered as an em dash, which would imply unknown dates
 * instead of an argument that is not about dates.
 */
function altRange(a: NonNullable<Entity["alternatives"]>[number]): string | null {
  const { start_year: s, end_year: e } = a;
  if (s === undefined || s === null) return null;
  if (e === undefined || e === null) return formatYear(s);
  return `${formatYear(s)} \u2013 ${formatYear(e)}`;
}

/**
 * The research handoff.
 *
 * The link is generated from the entity rather than authored, so every entity
 * has one — see `research/handoff`. The URL is also rendered as selectable
 * text, because opened offline the link goes nowhere and the user's fallback
 * is to write the search down and run it later. That is the module's stated
 * offline contract, and it only holds if the URL is actually on screen.
 *
 * ARCHITECTURE.md §10: user-initiated, new tab, `rel="noopener noreferrer"`,
 * descriptive text, no tracking parameters. Nothing here is fetched by the
 * app, so the footer's "no network requests" claim still holds.
 */
function renderHandoff(entity: Entity, cited: boolean): HTMLElement {
  const box = el("div", { class: "handoff", "data-testid": "panel-handoff-root" });
  box.append(el("div", { class: "handoff-head" }, "Start your research"));
  for (const t of handoffTargets(entity, index, { ambiguous })) {
    box.append(
      el(
        "a",
        {
          class: "handoff-link",
          href: t.url,
          target: "_blank",
          rel: "noopener noreferrer",
          "data-testid": `link-handoff-${t.id}`,
        },
        t.label,
      ),
    );
    box.append(
      el("code", { class: "handoff-url", "data-testid": `text-handoff-url-${t.id}` }, t.displayUrl),
    );
  }
  box.append(
    el(
      "p",
      { class: "handoff-note" },
      cited
        ? "The sources above are where this date comes from. This search is for everything else."
        : "This date is not yet sourced in the dataset. Treat it as a starting point and verify it.",
    ),
  );
  return box;
}


/**
 * The multi-calendar readout.
 *
 * A Gregorian year maps to a *span* in any calendar whose year does not begin
 * on 1 January, so readings are rendered as spans rather than points. Every
 * reading carries its own validity, because a conversion that is computable is
 * not necessarily meaningful: the polyfill will return a Persian year for a
 * Bronze Age date without complaint.
 */
function renderCalendarRows(entity: Entity): HTMLElement | null {
  if (entity.start_year === null) return null;

  // An uncalibrated radiocarbon age is not a calendar date and cannot be made
  // into one by arithmetic. Every calendar here would happily return a number,
  // and every one of them would be fabricated, so the whole panel refuses
  // rather than showing a row of confident wrong answers.
  const startValue = datingOf(entity).start?.primary.value;
  if (startValue !== undefined && !isCalendarConvertible(startValue)) {
    const box = el("div", { class: "calendars", "data-testid": "panel-calendar-readout" });
    box.append(el("div", { class: "calendars-head" }, "No calendar reading"));
    box.append(
      el(
        "p",
        { class: "cal-refusal" },
        "This date is in uncalibrated radiocarbon years, which are not calendar years. " +
          "Converting it would invent a precision the measurement does not have. " +
          "A calibrated age is needed before any calendar can be shown.",
      ),
    );
    return box;
  }

  const iso = isoFromHistorical(asHistorical(entity.start_year));
  const readings = readYearIn(iso, state.calendars);

  const box = el("div", { class: "calendars", "data-testid": "panel-calendar-readout" });
  box.append(
    el(
      "div",
      { class: "calendars-head" },
      `Start of period in ${readings.length} calendar${readings.length === 1 ? "" : "s"}`,
    ),
  );
  const list = el("dl", { class: "calendar-list" });
  for (const r of readings) {
    const def = getCalendar(r.calendarId);
    const dt = el("dt", {}, def?.name ?? r.calendarId);
    const dd = el("dd", {
      dir: "auto",
      "data-testid": `text-calendar-${r.calendarId}`,
      ...(r.note === undefined ? {} : { title: r.note }),
    });
    dd.append(el("span", { class: "cal-value" }, r.label));
    if (r.validity !== "ok") {
      dd.append(el("span", { class: `cal-flag cal-${r.validity}` }, flagLabel(r)));
    }
    list.append(dt, dd);
  }
  box.append(list);
  return box;
}

function flagLabel(r: CalendarReading): string {
  switch (r.validity) {
    case "proleptic":
      return "extrapolated";
    case "outside-range":
      return "not computed";
    case "deep-time":
      return "before calendars";
    default:
      return "";
  }
}

function renderCalendarPicker(): HTMLElement {
  const wrap = el("div", { class: "cal-picker" });
  const btn = el(
    "button",
    {
      type: "button",
      class: "cal-picker-toggle",
      "aria-expanded": String(state.calendarPickerOpen),
      "data-testid": "button-calendar-picker",
    },
    `Calendars (${state.calendars.length})`,
  );
  btn.addEventListener("click", () => {
    state.calendarPickerOpen = !state.calendarPickerOpen;
    render();
  });
  wrap.append(btn);

  if (!state.calendarPickerOpen) return wrap;

  const panel = el("div", { class: "cal-picker-panel", role: "group",
    "aria-label": "Calendars to display", "data-testid": "panel-calendar-picker" });
  let lastGroup = "";
  for (const c of CALENDARS) {
    if (c.group !== lastGroup) {
      panel.append(el("div", { class: "cal-group" }, c.group === "primary" ? "Widely used" : "Other systems"));
      lastGroup = c.group;
    }
    const on = state.calendars.includes(c.id);
    const row = el("button", {
      type: "button",
      class: "cal-option",
      role: "checkbox",
      "aria-checked": String(on),
      "data-testid": `option-calendar-${c.id}`,
      ...(c.note === undefined ? {} : { title: c.note }),
    });
    row.append(
      el("span", { class: "cal-check", "aria-hidden": "true" }, on ? "\u25A0" : "\u25A1"),
      el("span", {}, c.name),
    );
    row.addEventListener("click", () => {
      state.calendars = toggleCalendar(state.calendars, c.id);
      syncHash();
      render();
    });
    panel.append(row);
  }
  wrap.append(panel);
  return wrap;
}

function renderHeader(): HTMLElement {
  const head = el("header");
  head.append(el("h1", {}, "History & Prehistory"));
  head.append(
    el("span", { class: "version", "data-testid": "text-app-version" }, `v${APP_VERSION} \u00B7 data ${datasetVersion}`),
  );
  head.append(el("span", { class: "spacer" }));

  const controls = el("div", { class: "controls" });

  const search = el("input", {
    type: "search",
    placeholder: "Search eras, dynasties, rulers\u2026",
    "aria-label": "Search the historical tree",
    "data-testid": "input-search-query",
  }) as HTMLInputElement;
  search.value = state.query;
  search.addEventListener("input", () => {
    state.query = search.value;
    render();
    (document.querySelector('[data-testid="input-search-query"]') as HTMLInputElement | null)?.focus();
  });
  controls.append(search);

  const ctxToggle = el("button", {


    type: "button",


    class: `toggle${state.contextOpen ? " is-on" : ""}`,


    "data-testid": "button-toggle-context",


    "aria-pressed": state.contextOpen ? "true" : "false",


  }, "In context");


  ctxToggle.addEventListener("click", () => {


    state.contextOpen = !state.contextOpen;


    render();


  });


  const tier = el("select", {
    "aria-label": "Level of detail",
    "data-testid": "select-detail-tier",
  }) as HTMLSelectElement;
  for (const [value, label] of [
    ["foundational", "Essentials"],
    ["intermediate", "Standard"],
    ["specialist", "Everything"],
  ] as const) {
    const opt = el("option", { value }, label) as HTMLOptionElement;
    if (state.tier === value) opt.selected = true;
    tier.append(opt);
  }
  tier.addEventListener("change", () => {
    state.tier = tier.value as Tier;
    render();
  });
  controls.append(tier);
  controls.append(ctxToggle);
  controls.append(renderCalendarPicker());

  head.append(controls);
  return head;
}

function renderFooter(): HTMLElement {
  return el(
    "footer",
    { "data-testid": "panel-footer-root" },
    el("span", {}, `${entities.length.toLocaleString("en-US")} entities`),
    el("span", {}, "No data stored \u00B7 no network requests"),
    el(
      "a",
      { href: REPO_URL, target: "_blank", rel: "noopener noreferrer", "data-testid": "link-footer-repo" },
      "Source & dataset (MIT)",
    ),
  );
}

/**
 * The focus+context lens.
 *
 * Space allocated per row varies with degree of interest, and typography
 * reinforces it; position stays monotonic in time. That is Q-7 settled: a
 * hyperbolic disk needs sibling order to be free so children can be placed
 * radially, and here sibling order is temporal and is the information. Heian's
 * 88 nengō are a strict sequence — fanning them round a disk would destroy the
 * one relationship a reader needs.
 *
 * The focus is the current selection (Q-8), so clicking a row moves both.
 */
function renderContext(): HTMLElement | null {
  if (!state.contextOpen) return null;
  const focus = selected();
  const box = el("div", { class: "context", "data-testid": "panel-context-lens" });
  box.append(el("div", { class: "context-head" }, "In context"));

  if (!focus || focus.start_year === null) {
    box.append(el("p", { class: "context-empty" }, "Select a dated entity to see what surrounds it."));
    return box;
  }

  const neighbours = contextNeighbours(entities, focus, state.contextBudget, index);
  const top = neighbours[0]?.score ?? 0;
  const bottom = neighbours[neighbours.length - 1]?.score ?? top - 1;
  const list = el("div", { class: "context-body", role: "listbox", "data-testid": "list-context" });

  for (const n of neighbours) {
    // Normalized interest drives size, weight and opacity together, so the
    // falloff reads as one gradient rather than three effects.
    const t = bottom === top ? 1 : (n.score - bottom) / (top - bottom);
    const row = el("div", {
      class: `context-row${n.entity.id === focus.id ? " is-focus" : ""}${n.elsewhere ? " is-elsewhere" : ""}`,
      role: "option",
      "aria-selected": n.entity.id === focus.id ? "true" : "false",
      "data-testid": `option-context-${n.entity.id}`,
      style: `--doi:${t.toFixed(3)}`,
    });
    row.append(el("span", { class: "context-name" }, n.entity.name));
    row.append(el("span", { class: "context-when" }, displayRange(n.entity).text));
    row.addEventListener("click", () => selectEntity(n.entity.id));
    list.append(row);
  }
  box.append(list);

  const budget = el("label", { class: "context-budget" }, "Detail ");
  const input = el("input", {
    type: "range", min: "8", max: "60", step: "4",
    value: String(state.contextBudget),
    "data-testid": "input-context-budget",
    "aria-label": "How much context to show",
  }) as HTMLInputElement;
  input.addEventListener("input", () => {
    state.contextBudget = Number(input.value);
    render();
  });
  budget.append(input);
  budget.append(el("span", { class: "context-count" }, `${neighbours.length}`));
  box.append(budget);
  return box;
}

function render(): void {
  const app = document.querySelector<HTMLDivElement>("#app");
  if (!app) return;
  // The lens sits BESIDE the columns, not below them. Stacking it cost the
  // columns 67px of height, which is enough to push rows out of a long column
  // like Heian's 88 nengo - and "a second view alongside the Miller columns"
  // was the design intent anyway.
  const ctx = renderContext();
  const workspace = el("div", { class: "workspace" }, );
  workspace.append(renderColumns());
  if (ctx) workspace.append(ctx);
  app.replaceChildren(renderHeader(), workspace, renderReadout(), renderFooter());
}

/**
 * Re-read the selection when the fragment changes.
 *
 * Without this the URL is write-only: pasting a link with `#cal=...` into an
 * already-open tab, or using the back button after changing calendars, would
 * silently do nothing. Since the fragment is the app's only persistence
 * mechanism, it has to work in both directions.
 */
window.addEventListener("hashchange", () => {
  const next = parseSelection(window.location.hash);
  if (next.join(",") !== state.calendars.join(",")) {
    state.calendars = next;
    render();
  }
});

render();
