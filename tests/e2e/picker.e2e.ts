import { expect, test } from "@playwright/test";

// Every test runs against the built single-file artifact over file://.
// baseURL is set in playwright.config.ts.

test.beforeEach(async ({ page }) => {
  await page.goto("index.html");
});

test("boots offline from file:// with no network requests", async ({ page }) => {
  const requests: string[] = [];
  page.on("request", (r) => {
    if (!r.url().startsWith("file://")) requests.push(r.url());
  });
  await page.reload();
  await expect(page.getByTestId("root-app-shell")).toBeVisible();
  expect(requests).toEqual([]);
});

test("shows the version stamp and entity count", async ({ page }) => {
  // Both versions are pinned. They move independently, and the app version
  // silently drifting out of the header is exactly the kind of thing that
  // goes unnoticed until a bug report quotes a version that never shipped.
  // The two tracks had been asserted the wrong way round since the renumbering:
  // v0.5.0 is the DATA version and 3.1.0 was the APP version. The test was
  // failing for that reason, not because the header was wrong.
  await expect(page.getByTestId("text-app-version")).toContainText("v3.26.0.0");
  await expect(page.getByTestId("text-app-version")).toContainText("data 0.27.0.0");
  await expect(page.getByTestId("panel-footer-root")).toContainText("1,653 entities");
});

test("drills Region -> Era -> Period through the columns", async ({ page }) => {
  await page.getByTestId("select-detail-tier").selectOption("specialist");
  await page.getByTestId("option-tree-node-east-asia").click();
  await expect(page.getByTestId("region-column-1")).toBeVisible();
  await page.getByTestId("option-tree-node-east-asia.japan").click();
  await expect(page.getByTestId("region-column-2")).toBeVisible();
  await expect(page.getByTestId("text-readout-name")).toHaveText("Japan");
  await expect(page.getByTestId("text-readout-breadcrumb")).toContainText("East Asia");
});

test("search jumps to a node and rebuilds its full path", async ({ page }) => {
  await page.getByTestId("input-search-query").fill("Meiji");
  await expect(page.getByTestId("list-search-results")).toBeVisible();
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  await expect(page.getByTestId("text-readout-name")).toContainText("Meiji");
  await expect(page.getByTestId("text-readout-breadcrumb")).toContainText("\u203A");
});

test("search is diacritic-insensitive", async ({ page }) => {
  await page.getByTestId("input-search-query").fill("jomon");
  await expect(page.getByTestId("list-search-results").getByRole("option").first()).toContainText(
    "J\u014dmon",
  );
});

test("detail tier filters the visible tree", async ({ page }) => {
  await page.getByTestId("select-detail-tier").selectOption("specialist");
  await page.getByTestId("option-tree-node-east-asia").click();
  const wide = await page.getByTestId("region-column-1").getByRole("option").count();
  await page.getByTestId("select-detail-tier").selectOption("foundational");
  const narrow = await page.getByTestId("region-column-1").getByRole("option").count();
  expect(narrow).toBeLessThan(wide);
});

test("persists nothing across a reload", async ({ page }) => {
  await page.getByTestId("option-tree-node-east-asia").click();
  await expect(page.getByTestId("text-readout-name")).toHaveText("East Asia");
  await page.reload();
  await expect(page.getByTestId("panel-readout-root")).toContainText("Select a region to begin");
});

// Calendars are only shown for a DATED node. Region nodes carry no dates —
// "East Asia" has no start year — so the readout has nothing to convert and
// correctly renders no calendar block at all.
const openEdo = async (page: import("@playwright/test").Page): Promise<void> => {
  await page.getByTestId("option-tree-node-east-asia").click();
  await page.getByTestId("option-tree-node-east-asia.japan").click();
  await page.getByTestId("option-tree-node-east-asia.japan.edo").click();
};

test("shows no calendar block for an undated region node", async ({ page }) => {
  await page.getByTestId("option-tree-node-east-asia").click();
  await expect(page.getByTestId("panel-calendar-readout")).toHaveCount(0);
});

test("shows the selected calendars for a dated node", async ({ page }) => {
  await openEdo(page);
  await expect(page.getByTestId("panel-calendar-readout")).toBeVisible();
  await expect(page.getByTestId("text-calendar-common")).toBeVisible();
});

test("adds a second calendar and keeps it in the URL", async ({ page }) => {
  await openEdo(page);
  await page.getByTestId("button-calendar-picker").click();
  await page.getByTestId("option-calendar-islamic").click();
  await expect(page.getByTestId("text-calendar-islamic")).toBeVisible();
  // Persistence is the user's choice: it lives in the fragment, not storage.
  expect(page.url()).toContain("cal=common,islamic");
});

test("renders a lunar year as a span, not a point", async ({ page }) => {
  await page.goto("index.html#cal=islamic");
  await openEdo(page);
  // The Hijri year does not begin in January, so 1603 CE straddles two AH years.
  await expect(page.getByTestId("text-calendar-islamic")).toContainText("\u2013");
});

test("flags a conversion made before the calendar existed", async ({ page }) => {
  await page.goto("index.html#cal=persian");
  await page.getByTestId("option-tree-node-west-asia").click();
  await page.getByTestId("option-tree-node-west-asia.mesopotamia").click();
  await page.getByTestId("option-tree-node-west-asia.mesopotamia.sumerian").click();
  // Sumer predates the Persian epoch by three millennia. The polyfill will
  // return a number regardless; the readout must say it is extrapolated.
  await expect(page.getByTestId("panel-calendar-readout")).toContainText("extrapolated");
});

test("restores a calendar selection from the URL", async ({ page }) => {
  await page.goto("index.html#cal=common,hebrew,julian");
  await openEdo(page);
  await expect(page.getByTestId("text-calendar-hebrew")).toBeVisible();
  await expect(page.getByTestId("text-calendar-julian")).toBeVisible();
  await expect(page.getByTestId("button-calendar-picker")).toContainText("3");
});

test("still stores nothing across a reload", async ({ page }) => {
  await page.goto("index.html");
  await page.getByTestId("button-calendar-picker").click();
  await page.getByTestId("option-calendar-hebrew").click();
  await page.goto("index.html");
  await openEdo(page);
  await expect(page.getByTestId("text-calendar-hebrew")).toHaveCount(0);
});

test("renders deep time in Ma and ka, not seven-digit BCE", async ({ page }) => {
  // The naive formatter would print the origin of the genus as "2798051 BCE":
  // a year-precise position in a calendar that did not exist.
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.prehistory.hominins").click();
  await expect(page.getByTestId("text-readout-range")).toContainText("Ma");
  await expect(page.getByTestId("text-readout-range")).not.toContainText("BCE");
});

test("quotes a range in one unit where both ends fit it", async ({ page }) => {
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.paleolithic").click();
  await page.getByTestId("option-tree-node-global.paleolithic.magdalenian").click();
  // One unit AND one suffix for the whole range: "21.2 - 14.6 ka cal BP".
  // Not "21.2 ka - 14,610 BP", and not "21.2 ka cal BP - 14.6 ka cal BP".
  await expect(page.getByTestId("text-readout-range")).toHaveText(
    /^[\d.,]+ \u2013 [\d.,]+ ka cal BP$/,
  );
});

test("reaches the hominin branch", async ({ page }) => {
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.prehistory.hominins").click();
  await page.getByTestId("option-tree-node-global.prehistory.hominins.homo-sapiens").click();
  await expect(page.getByTestId("text-readout-name")).toHaveText("Homo sapiens");
  // Extant, so the range says present rather than a date.
  await expect(page.getByTestId("text-readout-range")).toContainText("present");
});

test("says unknown, not present, when an end was never dated", async ({ page }) => {
  // H. luzonensis is specialist tier and hidden at the default detail level.
  await page.getByTestId("select-detail-tier").selectOption("specialist");
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.prehistory.hominins").click();
  const luzon = page.getByTestId("option-tree-node-global.prehistory.hominins.homo-luzonensis");
  await luzon.scrollIntoViewIfNeeded();
  await luzon.click();
  await expect(page.getByTestId("text-readout-range")).toContainText("unknown");
});

test("shows no calendar reading for a deep-time date", async ({ page }) => {
  // 2.6 Ma is outside the date regime entirely: no calendar reaches it, and
  // the readout must say so rather than extrapolating.
  await page.goto("index.html#cal=common,islamic");
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.paleolithic").click();
  await page.getByTestId("option-tree-node-global.paleolithic.oldowan").click();
  await expect(page.getByTestId("panel-calendar-readout")).toContainText("before calendars");
});

test("shows the behavioural floor as a threshold, not a site", async ({ page }) => {
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.prehistory.firsts").click();
  const k = page.getByTestId("option-tree-node-global.prehistory.firsts.stone-knapping");
  await k.scrollIntoViewIfNeeded();
  await k.click();
  await expect(page.getByTestId("text-readout-name")).toHaveText("Stone Knapping");
  await expect(page.getByTestId("list-readout-facts")).toContainText("Earliest known");
  // One-sided: a floor with no end, not an interval.
  await expect(page.getByTestId("text-readout-range")).toContainText("3.3 Ma");
});

test("the lens shows what surrounded the focus", async ({ page }) => {
  await page.getByTestId("select-detail-tier").selectOption("specialist");
  await page.getByTestId("button-toggle-context").click();
  for (const id of [
    "global", "east-asia", "east-asia.japan",
    "east-asia.japan.heian", "east-asia.japan.heian.kohei",
  ]) {
    const n = page.getByTestId(`option-tree-node-${id}`);
    await n.scrollIntoViewIfNeeded();
    await n.click();
  }
  const rows = page.locator('[data-testid^="option-context-"]');
  await expect(rows.first()).toContainText("Kōhei");
  // Adjacent nengō, ranked by time rather than by tier: all 88 Heian children
  // share one tier, so tier can contribute nothing here.
  await expect(rows.nth(2)).toContainText("Tengi");
});

test("the lens reaches contemporaries in other branches", async ({ page }) => {
  // The thing Miller columns can never show, and the reason Q-8 did not need
  // a separately draggable lens.
  await page.getByTestId("select-detail-tier").selectOption("specialist");
  await page.getByTestId("button-toggle-context").click();
  for (const id of [
    "global", "east-asia", "east-asia.japan",
    "east-asia.japan.heian", "east-asia.japan.heian.kohei",
  ]) {
    const n = page.getByTestId(`option-tree-node-${id}`);
    await n.scrollIntoViewIfNeeded();
    await n.click();
  }
  await page.getByTestId("input-context-budget").fill("40");
  await page.getByTestId("input-context-budget").dispatchEvent("input");
  // Kohei is a Heian era of 1058-1065, so its contemporaries in China are the
  // Northern Song and the states that shared the period with it. Asserting the
  // FIRST row was brittle -- adding Western Xia legitimately reordered it. What
  // matters is that the lens reaches the other branch at all, and that adding
  // the Song's neighbours made the picture more complete rather than less.
  const elsewhere = page.locator(".context-row.is-elsewhere");
  await expect(elsewhere.filter({ hasText: "Song Dynasty" }).first()).toBeVisible();
  await expect(elsewhere.filter({ hasText: "Western Xia" }).first()).toBeVisible();
});

test("clicking in the lens moves the selection", async ({ page }) => {
  // Q-8: one focus, two ways to move it.
  await page.getByTestId("button-toggle-context").click();
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  const row = page.locator('[data-testid^="option-context-"]').nth(1);
  const name = (await row.locator(".context-name").textContent()) ?? "";
  await row.click();
  await expect(page.getByTestId("text-readout-name")).toHaveText(name);
});

test("the budget replaces the tier filter as the amount control", async ({ page }) => {
  await page.getByTestId("button-toggle-context").click();
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("input-context-budget").fill("8");
  await page.getByTestId("input-context-budget").dispatchEvent("input");
  await expect(page.locator('[data-testid^="option-context-"]')).toHaveCount(8);
});

test("offers a generated Wikipedia handoff for the selected entity", async ({ page }) => {
  // The link is generated per entity rather than authored, so the assertion is
  // on shape and on the §10 link contract, not on a curated URL.
  await page.getByTestId("option-tree-node-east-asia").click();
  await page.getByTestId("option-tree-node-east-asia.japan").click();

  const link = page.getByTestId("link-handoff-wikipedia");
  await expect(link).toBeVisible();
  await expect(link).toHaveText(/^Search Wikipedia for /);
  await expect(link).toHaveAttribute("href", /^https:\/\/en\.wikipedia\.org\/w\/index\.php\?search=Japan$/);
  await expect(link).toHaveAttribute("target", "_blank");
  await expect(link).toHaveAttribute("rel", "noopener noreferrer");

  // The URL is deliberately NOT printed on screen. It was, until a percent-
  // encoded search string on every entity proved to be pure noise. The offline
  // fallback moved into the downloadable research note, which is where a user
  // without a network can actually keep it.
  await expect(page.getByTestId("text-handoff-url-wikipedia")).toHaveCount(0);
});

test("disambiguates a repeated name in the handoff query", async ({ page }) => {
  // Two Emperor Taizongs exist in the dataset; the nearest ancestor that adds
  // signal is appended so the search does not land on a disambiguation page.
  await page.getByTestId("input-search-query").fill("Emperor Taizong");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  await expect(page.getByTestId("link-handoff-wikipedia")).toHaveText(
    /Search Wikipedia for .Emperor Taizong \w+/,
  );
});

test("the handoff makes no network request of its own", async ({ page }) => {
  const external: string[] = [];
  page.on("request", (r) => {
    if (!r.url().startsWith("file://")) external.push(r.url());
  });
  await page.getByTestId("option-tree-node-east-asia").click();
  await expect(page.getByTestId("link-handoff-wikipedia")).toBeVisible();
  expect(external).toEqual([]);
});

test("shows caveats and competing dates, which nothing rendered before", async ({ page }) => {
  // 62 entities carried caveats and 56 carried alternatives that no code path
  // read. This asserts the epistemic layer actually reaches the screen.
  await page.getByTestId("input-search-query").fill("Neolithic Transition");
  await page.getByTestId("list-search-results").getByRole("option").first().click();

  const caveats = page.getByTestId("panel-caveats-root");
  await expect(caveats).toContainText("Common misconception");
  await expect(caveats).toContainText("Not a revolution and not an event");

  const alts = page.getByTestId("panel-alternatives-root");
  await expect(alts).toContainText("Minority view");
  await expect(alts).toContainText("Abbo and Gopher");
});

test("marks a superseded rival claim as superseded", async ({ page }) => {
  // Botai is still widely cited as the origin of domestic horses. It must not
  // read as a live competitor to the Volga-Don date.
  await page.getByTestId("input-search-query").fill("Horse Domestication");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  const alts = page.getByTestId("panel-alternatives-root");
  await expect(alts).toContainText("Botai husbandry");
  await expect(alts).toContainText("Superseded");
  await expect(alts).toContainText("3500 BCE");
});

test("omits the range when a rival claim is not about dates", async ({ page }) => {
  // The Abbo-Gopher dispute is about the shape of the transition, not its
  // years. An em dash there would imply unknown dates instead of an argument.
  await page.getByTestId("input-search-query").fill("Neolithic Transition");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  await expect(page.getByTestId("panel-alternatives-root").locator(".alt-range")).toHaveCount(0);
});

test("renders the sources a date rests on, numbered per entity", async ({ page }) => {
  await page.getByTestId("input-search-query").fill("Neolithic Transition");
  await page.getByTestId("list-search-results").getByRole("option").first().click();

  const sources = page.getByTestId("panel-sources-root");
  await expect(sources).toContainText("Quaternary Science Reviews");
  await expect(sources).toContainText("Peer-reviewed");

  // The citation link is the descriptive text, per ARCHITECTURE.md §10, and the
  // bare URL is separate so it survives being opened offline.
  const cite = sources.locator("a.source-cite").first();
  await expect(cite).toHaveAttribute("target", "_blank");
  await expect(cite).toHaveAttribute("rel", "noopener noreferrer");
  await expect(sources.locator(".source-url").first()).toContainText("sciencedirect.com");
});

test("numbers citations per entity rather than globally", async ({ page }) => {
  // A global scheme would show "[147]" on a panel listing three sources.
  await page.getByTestId("input-search-query").fill("Horse Domestication");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  const marks = await page.locator(".cite").allTextContents();
  expect(marks.length).toBeGreaterThan(0);
  for (const m of marks) {
    for (const n of m.replace(/[[\]]/g, "").split(",")) {
      expect(Number(n)).toBeLessThanOrEqual(4);
    }
  }
});

test("ties a caveat to the source that backs it", async ({ page }) => {
  await page.getByTestId("input-search-query").fill("Neolithic Transition");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  // The "contested centres" caveat rests on the Harlan/Vavilov/Purugganan
  // review, which must be reachable from the caveat by its number.
  const caveats = page.getByTestId("panel-caveats-root");
  await expect(caveats.locator(".cite")).toHaveCount(2);
});

test("says so when a date is not sourced, instead of implying it is", async ({ page }) => {
  // The handoff used to claim, on every entity, that dates were "not a
  // citation". That is now only true of the uncited ones.
  await page.getByTestId("option-tree-node-europe").click();
  const handoff = page.getByTestId("panel-handoff-root");
  await expect(handoff).toContainText("not yet sourced");

  await page.getByTestId("input-search-query").fill("Neolithic Transition");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  await expect(page.getByTestId("panel-handoff-root")).toContainText(
    "sources above are where this date comes from",
  );
});

test("makes no network request when rendering citations", async ({ page }) => {
  const external: string[] = [];
  page.on("request", (r) => {
    if (!r.url().startsWith("file://")) external.push(r.url());
  });
  await page.getByTestId("input-search-query").fill("Neolithic Transition");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  await expect(page.getByTestId("panel-sources-root")).toBeVisible();
  expect(external).toEqual([]);
});

test("marks a received convention in the picker, not just in the panel", async ({ page }) => {
  // A caveat below the fact list does not reach a reader who scans the date
  // and moves on. Rome's 753 BCE used to render identically to a Bayesian
  // radiocarbon range.
  await page.getByTestId("input-search-query").fill("Roman Kingdom");
  const row = page.getByTestId("list-search-results").getByRole("option").first();
  await expect(row).toContainText("\u2020");

  await row.click();
  const banner = page.getByTestId("panel-standing-banner");
  await expect(banner).toContainText("Received convention, not a finding");
});

test("quotes a received convention in calendar years, never in BP", async ({ page }) => {
  // BP is the idiom of radiometric measurement. Rendering a pottery-typology
  // convention as "6,749 BP" lends it authority and invents a digit.
  await page.getByTestId("input-search-query").fill("Namazga");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  const range = page.getByTestId("text-readout-range");
  await expect(range).toContainText("4800 BCE");
  await expect(range).not.toContainText("BP");
});

test("leads with the warning, above the summary", async ({ page }) => {
  await page.getByTestId("input-search-query").fill("Namazga");
  await page.getByTestId("list-search-results").getByRole("option").first().click();
  const order = await page.evaluate(() => {
    const root = document.querySelector('[data-testid="panel-readout-root"]')!;
    return [...root.children].map((c) => c.getAttribute("data-testid") ?? c.className);
  });
  const banner = order.indexOf("panel-standing-banner");
  const facts = order.indexOf("list-readout-facts");
  expect(banner).toBeGreaterThan(-1);
  expect(banner).toBeLessThan(facts);
});

test("shows a point event as a single date in both the gutter and the readout", async ({ page }) => {
  // Point events arrived in 0.16.0.0 and immediately exposed that TWO separate
  // formatters handle a missing end year, and both defaulted to "ongoing". The
  // Narmer Palette read "5,049 BP - present" in the panel and Kadesh read
  // "1274 BCE-" in the column. A battle is a moment, not an open interval.
  await page.getByTestId("input-search-query").fill("Battle of Kadesh");
  await page.waitForTimeout(400);
  const gutter = await page.getByTestId("region-picker-columns").innerText();
  expect(gutter).toContain("1274");
  expect(gutter).not.toMatch(/1274\u2009BCE\u2013/);

  await page.getByText("Battle of Kadesh", { exact: false }).last().click();
  await page.waitForTimeout(400);
  const panel = await page.getByTestId("panel-readout-root").innerText();
  expect(panel).not.toContain("present");
});
