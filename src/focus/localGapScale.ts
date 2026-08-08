/**
 * Median gap between neighbouring entity midpoints around a given year.
 *
 * This is the density normalizer, and it is why the lens can work at both ends
 * of the dataset. Entity density spans six orders of magnitude — 0.001 per
 * thousand years in deep time against 680 in the last century — and the local
 * median gap runs from about 75,000 years down to 1. Any radius stated in
 * absolute years is therefore wrong by four orders of magnitude at one end no
 * matter where it is tuned.
 *
 * Dividing a raw year-distance by this turns "500 years away" into "about n
 * neighbours away", which means the same thing over the Pleistocene as it does
 * over the Cold War.
 */
export function localGapScale(
  sortedMidpoints: readonly number[],
  year: number,
  window = 25,
): number {
  let lo = 0;
  let hi = sortedMidpoints.length;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if ((sortedMidpoints[mid] as number) < year) lo = mid + 1;
    else hi = mid;
  }
  const slice = sortedMidpoints.slice(
    Math.max(0, lo - window),
    Math.min(sortedMidpoints.length, lo + window),
  );
  const gaps: number[] = [];
  for (let i = 1; i < slice.length; i += 1) {
    const d = (slice[i] as number) - (slice[i - 1] as number);
    if (d > 0) gaps.push(d);
  }
  if (gaps.length === 0) return 1000;
  gaps.sort((a, b) => a - b);
  return Math.max(gaps[gaps.length >> 1] as number, 0.5);
}
