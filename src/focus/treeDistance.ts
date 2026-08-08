import type { TreeIndex } from "../entity/tree";
import { pathTo } from "../entity/tree";

/** Hops between two nodes through their lowest common ancestor. */
export function treeDistance(index: TreeIndex, aId: string, bId: string): number {
  const upA = pathTo(index, aId).map((e) => e.id).reverse();
  const upB = pathTo(index, bId).map((e) => e.id).reverse();
  const posB = new Map(upB.map((id, i) => [id, i]));
  for (let i = 0; i < upA.length; i += 1) {
    const j = posB.get(upA[i] as string);
    if (j !== undefined) return i + j;
  }
  return upA.length + upB.length;
}
