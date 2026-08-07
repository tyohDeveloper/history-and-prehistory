/**
 * The calendar catalog.
 *
 * Two families live here:
 *
 *  - **Temporal-backed** calendars, carried over from OmniUnit's date
 *    category. Conversion and localized rendering come from the Temporal
 *    polyfill plus CLDR via `Intl.DateTimeFormat`.
 *  - **Arithmetic** calendars that Temporal does not implement but a history
 *    app genuinely needs: Julian and Revised Julian (JDN pivot), plus the
 *    epoch-offset and cyclic reckonings the entity dataset already declares
 *    (Roman AUC, Byzantine AM, Olympiad, sexagenary, Maya Long Count, Juche,
 *    French Republican).
 *
 * Every calendar declares a `validFrom` / `validTo` window in historical
 * Gregorian years. Outside that window a conversion is still *computable* —
 * Temporal will happily hand back Persian year -3921 for a Bronze Age date —
 * but it is not *meaningful*. The window is what lets the readout say so
 * instead of printing a confident absurdity. See `convert.ts`.
 */

export type CalendarGroup = "primary" | "variant";

export type Backend =
  | { kind: "temporal"; temporalId: string }
  | { kind: "julian" }
  | { kind: "revised-julian" }
  /** year = gregorianYear + offset, with no year zero in either scheme. */
  | { kind: "offset"; offset: number; suffix: string }
  | { kind: "olympiad" }
  | { kind: "sexagenary" }
  | { kind: "maya" };

export interface CalendarDef {
  id: string;
  /** Full name shown in the calendar picker. */
  name: string;
  /** Compact label shown on a readout line. */
  short: string;
  group: CalendarGroup;
  backend: Backend;
  /**
   * Meaningful range in historical Gregorian years (negative = BCE, no zero).
   * `null` on either end means unbounded in that direction.
   */
  validFrom: number | null;
  validTo: number | null;
  /** Why the window is where it is, or what to distrust inside it. */
  note?: string;
  sourceUrl: string;
}

/**
 * Ordering matters: `primary` calendars appear first in the picker, variants
 * after a divider. Same idiom as OmniUnit's primary/variant calendar groups —
 * broadly useful systems stay prominent without hiding the rest in a
 * separate tool.
 */
export const CALENDARS: readonly CalendarDef[] = [
  {
    id: "common",
    name: "Common Era (CE/BCE)",
    short: "CE/BCE",
    group: "primary",
    backend: { kind: "temporal", temporalId: "gregory" },
    validFrom: null,
    validTo: null,
    note: "The dataset's base reckoning. Proleptic Gregorian before 1582.",
    sourceUrl: "https://en.wikipedia.org/wiki/Common_Era",
  },
  {
    id: "gregorian",
    name: "Gregorian (AD/BC)",
    short: "AD/BC",
    group: "primary",
    backend: { kind: "temporal", temporalId: "gregory" },
    validFrom: null,
    validTo: null,
    note: "Same arithmetic as Common Era; Christian-era labels instead.",
    sourceUrl: "https://en.wikipedia.org/wiki/Gregorian_calendar",
  },
  {
    id: "julian",
    name: "Julian (Eastern Orthodox)",
    short: "Julian",
    group: "primary",
    backend: { kind: "julian" },
    validFrom: -45,
    validTo: null,
    note: "Introduced 45 BCE. Civil use in the West ends 1582; Orthodox use continues.",
    sourceUrl: "https://en.wikipedia.org/wiki/Julian_calendar",
  },
  {
    id: "hebrew",
    name: "Hebrew (Anno Mundi)",
    short: "AM",
    group: "primary",
    backend: { kind: "temporal", temporalId: "hebrew" },
    validFrom: -3760,
    validTo: null,
    note: "The fixed calculated calendar dates from roughly the 4th century CE; earlier years are retrojected.",
    sourceUrl: "https://en.wikipedia.org/wiki/Hebrew_calendar",
  },
  {
    id: "islamic",
    name: "Islamic (Umm al-Qura)",
    short: "AH",
    group: "primary",
    backend: { kind: "temporal", temporalId: "islamic-umalqura" },
    validFrom: 622,
    validTo: null,
    note: "Umm al-Qura is a Saudi administrative calendar; before 1300 AH it is an approximation of observed lunar months.",
    sourceUrl: "https://en.wikipedia.org/wiki/Islamic_calendar",
  },
  {
    id: "persian",
    name: "Persian (Solar Hijri)",
    short: "AP",
    group: "primary",
    backend: { kind: "temporal", temporalId: "persian" },
    validFrom: 622,
    validTo: null,
    note: "Adopted in its modern form in 1925; earlier years are retrojected.",
    sourceUrl: "https://en.wikipedia.org/wiki/Solar_Hijri_calendar",
  },
  {
    id: "japanese",
    name: "Japanese (nengō)",
    short: "Nengō",
    group: "primary",
    backend: { kind: "temporal", temporalId: "japanese" },
    validFrom: 645,
    validTo: null,
    note: "Era names begin with Taika (645). Pre-Meiji eras were lunisolar; CLDR maps them to Gregorian year boundaries, so month-level dates are approximate.",
    sourceUrl: "https://en.wikipedia.org/wiki/Japanese_era_name",
  },
  {
    id: "chinese",
    name: "Chinese (lunisolar)",
    short: "Chinese",
    group: "primary",
    backend: { kind: "temporal", temporalId: "chinese" },
    validFrom: -2637,
    validTo: null,
    note: "Historical Chinese calendars were reformed repeatedly; the modern algorithm retrojected is an approximation.",
    sourceUrl: "https://en.wikipedia.org/wiki/Chinese_calendar",
  },
  {
    id: "indian",
    name: "Indian national (Śaka)",
    short: "Śaka",
    group: "primary",
    backend: { kind: "temporal", temporalId: "indian" },
    validFrom: 78,
    validTo: null,
    note: "Śaka era epoch is 78 CE; the modern national calendar was adopted in 1957.",
    sourceUrl: "https://en.wikipedia.org/wiki/Indian_national_calendar",
  },
  {
    id: "buddhist",
    name: "Buddhist (Thai)",
    short: "BE",
    group: "primary",
    backend: { kind: "temporal", temporalId: "buddhist" },
    validFrom: -543,
    validTo: null,
    note: "Thailand's year start moved to 1 January only in 1941; earlier Thai dates need care.",
    sourceUrl: "https://en.wikipedia.org/wiki/Buddhist_calendar",
  },
  {
    id: "coptic",
    name: "Coptic (Anno Martyrum)",
    short: "AM (Copt.)",
    group: "primary",
    backend: { kind: "temporal", temporalId: "coptic" },
    validFrom: 284,
    validTo: null,
    note: "Epoch is the accession of Diocletian, 284 CE.",
    sourceUrl: "https://en.wikipedia.org/wiki/Coptic_calendar",
  },
  {
    id: "ethiopic",
    name: "Ethiopic (Amete Mihret)",
    short: "Eth.",
    group: "primary",
    backend: { kind: "temporal", temporalId: "ethiopic" },
    validFrom: 8,
    validTo: null,
    sourceUrl: "https://en.wikipedia.org/wiki/Ethiopian_calendar",
  },
  {
    id: "roman-auc",
    name: "Roman (ab urbe condita)",
    short: "AUC",
    group: "primary",
    backend: { kind: "offset", offset: 753, suffix: "AUC" },
    validFrom: -753,
    validTo: 1453,
    note: "Counted from the traditional founding of Rome, 753 BCE. A scholarly convention rather than a widely used Roman civil reckoning.",
    sourceUrl: "https://en.wikipedia.org/wiki/Ab_urbe_condita",
  },
  {
    id: "olympiad",
    name: "Greek Olympiad",
    short: "Ol.",
    group: "primary",
    backend: { kind: "olympiad" },
    validFrom: -776,
    validTo: 393,
    note: "Four-year cycles from 776 BCE. Olympiad years began in midsummer, so each maps across two Gregorian years.",
    sourceUrl: "https://en.wikipedia.org/wiki/Olympiad",
  },
  {
    id: "byzantine-am",
    name: "Byzantine (Anno Mundi)",
    short: "AM (Byz.)",
    group: "variant",
    backend: { kind: "offset", offset: 5508, suffix: "AM" },
    validFrom: -5508,
    validTo: 1700,
    note: "Year began 1 September, so a Gregorian year maps to two Byzantine years.",
    sourceUrl: "https://en.wikipedia.org/wiki/Byzantine_calendar",
  },
  {
    id: "chinese-sexagenary",
    name: "Chinese sexagenary cycle",
    short: "Ganzhi",
    group: "variant",
    backend: { kind: "sexagenary" },
    validFrom: -2637,
    validTo: null,
    note: "A 60-year stem-branch cycle. It names years but does not number them, so it is ambiguous without a dynasty or era.",
    sourceUrl: "https://en.wikipedia.org/wiki/Sexagenary_cycle",
  },
  {
    id: "maya-long-count",
    name: "Maya Long Count",
    short: "Long Count",
    group: "variant",
    backend: { kind: "maya" },
    validFrom: -3114,
    validTo: null,
    note: "Uses the GMT correlation (584283). Competing correlations shift dates by days to years.",
    sourceUrl: "https://en.wikipedia.org/wiki/Mesoamerican_Long_Count_calendar",
  },
  {
    id: "roc",
    name: "Minguo (Republic of China)",
    short: "民國",
    group: "variant",
    backend: { kind: "temporal", temporalId: "roc" },
    validFrom: 1912,
    validTo: null,
    sourceUrl: "https://en.wikipedia.org/wiki/Republic_of_China_calendar",
  },
  {
    id: "juche",
    name: "Juche (North Korea)",
    short: "Juche",
    group: "variant",
    backend: { kind: "offset", offset: -1911, suffix: "Juche" },
    validFrom: 1912,
    validTo: null,
    note: "Introduced 1997, counted from Kim Il-sung's birth in 1912.",
    sourceUrl: "https://en.wikipedia.org/wiki/North_Korean_calendar",
  },
  {
    id: "dangi",
    name: "Korean (Dangi)",
    short: "Dangi",
    group: "variant",
    backend: { kind: "temporal", temporalId: "dangi" },
    validFrom: -2333,
    validTo: null,
    sourceUrl: "https://en.wikipedia.org/wiki/Korean_calendar",
  },
  {
    id: "islamic-civil",
    name: "Islamic (tabular, civil epoch)",
    short: "AH (civil)",
    group: "variant",
    backend: { kind: "temporal", temporalId: "islamic-civil" },
    validFrom: 622,
    validTo: null,
    note: "Arithmetic rather than observational; drifts from observed months by a day or so.",
    sourceUrl: "https://en.wikipedia.org/wiki/Tabular_Islamic_calendar",
  },
  {
    id: "islamic-tbla",
    name: "Islamic (tabular, astronomical epoch)",
    short: "AH (astro.)",
    group: "variant",
    backend: { kind: "temporal", temporalId: "islamic-tbla" },
    validFrom: 622,
    validTo: null,
    sourceUrl: "https://en.wikipedia.org/wiki/Tabular_Islamic_calendar",
  },
  {
    id: "ethiopic-alem",
    name: "Ethiopic (Amete Alem)",
    short: "AA",
    group: "variant",
    backend: { kind: "temporal", temporalId: "ethioaa" },
    validFrom: null,
    validTo: null,
    sourceUrl: "https://en.wikipedia.org/wiki/Ethiopian_calendar",
  },
  {
    id: "revised-julian",
    name: "Revised Julian",
    short: "Rev. Julian",
    group: "variant",
    backend: { kind: "revised-julian" },
    validFrom: 1600,
    validTo: 2800,
    note: "Coincides exactly with Gregorian between 1600 and 2800; outside that window this build does not compute it.",
    sourceUrl: "https://en.wikipedia.org/wiki/Revised_Julian_calendar",
  },
  {
    id: "french-republican",
    name: "French Republican",
    short: "An",
    group: "variant",
    backend: { kind: "offset", offset: -1791, suffix: "An" },
    validFrom: 1792,
    validTo: 1805,
    note: "Year began at the autumn equinox, so a Gregorian year maps across two Republican years. Abolished 1806.",
    sourceUrl: "https://en.wikipedia.org/wiki/French_Republican_calendar",
  },
  {
    id: "iso8601",
    name: "ISO 8601 (astronomical years)",
    short: "ISO",
    group: "variant",
    backend: { kind: "temporal", temporalId: "iso8601" },
    validFrom: null,
    validTo: null,
    note: "Has a year zero: 1 BCE is 0000, 2 BCE is -0001. Differs by one from every other reckoning here.",
    sourceUrl: "https://en.wikipedia.org/wiki/ISO_8601",
  },
] as const;

export const CALENDARS_BY_ID: ReadonlyMap<string, CalendarDef> = new Map(
  CALENDARS.map((c) => [c.id, c]),
);

export function getCalendar(id: string): CalendarDef | undefined {
  return CALENDARS_BY_ID.get(id);
}

/** Calendars shown by default when the user has not chosen any. */
export const DEFAULT_CALENDAR_IDS: readonly string[] = ["common"];
