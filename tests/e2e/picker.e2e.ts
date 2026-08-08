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
  await expect(page.getByTestId("text-app-version")).toContainText("data 2.2.0");
  await expect(page.getByTestId("panel-footer-root")).toContainText("1,310 entities");
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

test("reaches the prehistory pilot and its deep-time dates", async ({ page }) => {
  // The five pilot entities are what proves Q-10 is unblocked end to end:
  // authored with schema 1.1.0 fields, validated, and reaching the UI.
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await expect(page.getByTestId("option-tree-node-global.prehistory.oldowan")).toBeVisible();
  await page.getByTestId("option-tree-node-global.prehistory.oldowan").click();
  await expect(page.getByTestId("text-readout-name")).toHaveText("Oldowan Industry");
});

test("shows no calendar reading for a deep-time date", async ({ page }) => {
  // 2.6 Ma is outside the date regime entirely: no calendar reaches it, and
  // the readout must say so rather than extrapolating.
  await page.goto("index.html#cal=common,islamic");
  await page.getByTestId("option-tree-node-global").click();
  await page.getByTestId("option-tree-node-global.prehistory").click();
  await page.getByTestId("option-tree-node-global.prehistory.oldowan").click();
  await expect(page.getByTestId("panel-calendar-readout")).toContainText("before calendars");
});
