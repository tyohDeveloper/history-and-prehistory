import { expect, test } from "@playwright/test";

// Every test runs against the built single-file artifact over file://.
// baseURL is set in playwright.config.ts.

test.beforeEach(async ({ page }) => {
  await page.goto("");
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
  await expect(page.getByTestId("text-app-version")).toContainText("data 2.1.0");
  await expect(page.getByTestId("panel-footer-root")).toContainText("1,305 entities");
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
