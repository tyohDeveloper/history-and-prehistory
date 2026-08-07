import "./style.css";
import { datasetVersion, entities } from "./lib/dataset";
import {
  buildIndex,
  childrenOf,
  formatRange,
  pathTo,
  searchEntities,
  visibleAtTier,
} from "./lib/tree";
import type { Entity, EntityKind, Tier } from "./lib/types";
import { readYearIn, type CalendarReading } from "./lib/calendars/convert";
import { CALENDARS, getCalendar } from "./lib/calendars/registry";
import { parseSelection, serializeSelection, toggleCalendar } from "./lib/calendarSelection";
import { asHistorical, isoFromHistorical } from "./lib/chrono/year";

const APP_VERSION = __APP_VERSION__;
const REPO_URL = "https://github.com/tyohDeveloper/history-and-prehistory";

const GLYPH: Record<EntityKind, string> = {
  region: "\u25A6",
  era: "\u25A3",
  period: "\u25C6",
  reign: "\u25CF",
  event: "\u25C7",
};

const KIND_LABEL: Record<EntityKind, string> = {
  region: "Region",
  era: "Era",
  period: "Period",
  reign: "Reign",
  event: "Event",
};

const index = buildIndex(entities);

interface State {
  /** Selected node per column depth; index 0 is the root column. */
  path: string[];
  tier: Tier;
  query: string;
  /** Calendars shown in the readout. Persisted only in location.hash. */
  calendars: string[];
  calendarPickerOpen: boolean;
}

const state: State = {
  path: [],
  tier: "intermediate",
  query: "",
  calendars: parseSelection(window.location.hash),
  calendarPickerOpen: false,
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
      title: `${KIND_LABEL[e.kind]} · ${formatRange(e)}`,
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
  box.append(el("div", { class: "range", "data-testid": "text-readout-range" }, formatRange(e)));
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
  if (e.date_note !== undefined) fact("Dating note", e.date_note);
  if (e.aliases !== undefined && e.aliases.length > 0) fact("Also known as", e.aliases.join(", "));
  if (e.calendar_ids !== undefined && e.calendar_ids.length > 0) {
    fact("Calendars", e.calendar_ids.join(", "));
  }
  if (e.capital !== undefined) fact("Capital", e.capital);
  box.append(dl);
  const calendars = renderCalendarRows(e);
  if (calendars !== null) box.append(calendars);
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

function render(): void {
  const app = document.querySelector<HTMLDivElement>("#app");
  if (!app) return;
  app.replaceChildren(renderHeader(), renderColumns(), renderReadout(), renderFooter());
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
