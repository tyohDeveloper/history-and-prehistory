# Brief: Korean rulers

Read `/home/user/workspace/hp/docs/briefs/COMMON.md` first. Write to
`/home/user/workspace/hp/docs/research/korea.json`.

Korea currently has **ten dynasties and zero rulers** in this dataset. Cover the most
consequential rulers only — roughly 22–28 people total, not complete king lists.

Group your output by adding a `"polity"` field to each object, one of exactly:
`three-kingdoms`, `unified-silla`, `goryeo`, `joseon`.

- **Three Kingdoms (57 BCE–668 CE)** — 6–8 figures across Goguryeo, Baekje and Silla.
  Include Gwanggaeto the Great, Jangsu, Seong of Baekje, Jinheung of Silla, Munmu.
  Say which kingdom each ruled in the summary; the dataset has one node for all three.
- **Unified Silla (668–935)** — 3–4, including Munmu if you place him here instead, and
  Sinmun or Gyeongdeok.
- **Goryeo (918–1392)** — 4–6, including Taejo Wang Geon, Gwangjong, Sejong'"'"'s
  predecessors are Joseon so do not stray, and the Mongol-period kings.
- **Joseon (1392–1897)** — 6–8, including Taejo Yi Seong-gye, **Sejong the Great**
  (Hangul), Seongjong, Yeonsangun, Seonjo (Imjin War), Yeongjo, Jeongjo, Gojong.

## Care points

- **Gojoseon** has no reliable ruler list. Do **not** invent one. If Dangun is the only
  named figure, return him as a single entry with `date_precision: "traditional"` and a
  `contested` note saying he is the mythological founder — or return nothing for Gojoseon
  and say why in a `"notes"` key at the top level of the JSON.
- Korean regnal names vs personal names: use the name a reader will recognise (Sejong the
  Great, not Yi Do), and put the other in `aliases`.
- Include Hangul in a `"native"` field where you can confirm it.
