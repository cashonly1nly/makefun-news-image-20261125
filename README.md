# makefun-news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/cashonly1nly/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/cashonly1nly/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up world news of Wednesday 25 November 2026, for make.fun bounty `news-image-20261125` ($100 total; 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20; deadline 2026-11-27 00:00 UTC, no entry fee).

## Run it

```sh
node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` locally).

---

<sub>Entered on [make.fun](https://make.fun/?ref=prprbmdv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>

## Files

- `main.ts` — Node 22, standard library only. Copies `entry.png` to the output dir.
- `entry.png` — the entry: 1024×1024 PNG, ~131 KB. A newspaper-style infographic: masthead with the date, six main stories, an "Also on 25 November" strip, and a sources line.
- `build_image.py` — the Python/PIL script that drew `entry.png` (not run by `main.ts`; kept for transparency).
- `NEWS_SOURCES.md` — the verified news and its sources.
- `LICENSE` — MIT.

## Stories in the image

1. Space — Shenzhou-24 carries the first Pakistani astronaut to Tiangong.
2. China — Beijing investigates Shanghai party chief Chen Jining.
3. Middle East — Second Houthi strike in a week hits Riyadh's tallest tower, 11 injured; Saudi-led coalition hits Hodeidah.
4. Europe — Overnight Russia–Ukraine strikes kill 3, injure 15; Ukraine seeks €115bn aid for 2027.
5. Americas — Colombia frees all hostages in the Cartagena supermarket siege.
6. Tech & Trade — US jury convicts Huawei of trade-secret theft and bank fraud.
Also: Bangladesh garment wage +36%, Indonesia mine rescue, North Korea expels a Swiss envoy in Pyongyang.

## Local verification (2026-11-25)

- `entry.png`: PNG, 1024×1024, 131,192 bytes (< 1 MiB), `PIL.verify()` OK.
- `main.ts` run twice locally into two output dirs: byte-identical `entry.png` in both (same sha256 as the repo file).
- Kit check with the Muse-app transcript bundle: 14 passed, 0 failed.
