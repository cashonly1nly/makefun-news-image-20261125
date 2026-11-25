# News image — 25 November 2026

One image summing up world news of Wednesday 25 November 2026, for
make.fun bounty `news-image-20261125` ($100 total; 1st $20, 2nd $12,
3rd $6, 4th–10th $2, 11th–50th $1.20; deadline 2026-11-27 00:00 UTC,
no entry fee).

## Files

- `main.ts` — Node 22, standard library only. Copies `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` locally).
- `entry.png` — the entry: 1024×1024 PNG, ~131 KB. A newspaper-style
  infographic: masthead with the date, six main stories, an
  "Also on 25 November" strip, and a sources line.
- `build_image.py` — the Python/PIL script that drew `entry.png`
  (not run by `main.ts`; kept for transparency).
- `NEWS_SOURCES.md` — the verified news and its sources.
- `LICENSE` — MIT.

## Stories in the image

1. Space — Shenzhou-24 carries the first Pakistani astronaut to Tiangong.
2. China — Beijing investigates Shanghai party chief Chen Jining.
3. Middle East — Second Houthi strike in a week hits Riyadh's tallest
   tower, 11 injured; Saudi-led coalition hits Hodeidah.
4. Europe — Overnight Russia–Ukraine strikes kill 3, injure 15;
   Ukraine seeks €115bn aid for 2027.
5. Americas — Colombia frees all hostages in the Cartagena
   supermarket siege.
6. Tech & Trade — US jury convicts Huawei of trade-secret theft
   and bank fraud.
Also: Bangladesh garment wage +36%, Indonesia mine rescue,
North Korea expels a Swiss envoy in Pyongyang.

## Local verification (2026-11-25 21:1x CST)

- `entry.png`: PNG, 1024×1024, 131,192 bytes (< 1 MiB), `PIL.verify()` OK.
- `main.ts` run twice locally into two output dirs: byte-identical
  `entry.png` in both (same sha256 as the repo file).

## Harness / paid-eligibility — READ THIS BEFORE SUBMITTING

This entry was built in Muse, whose sessions are NOT recorded in a
format the make.fun kit `bundle` can read. All bounties on make.fun
have `handed_over_places=none`: an entry submitted with only a
handed-over Muse transcript is ranked but takes **no paid place**.

To make it paid-eligible, the build (writing/editing `main.ts`,
`build_image.py`, `entry.png`) must be re-done inside a recorded
harness — Codex (installed here as `codex` 0.164, but **not logged
in**), Gemini CLI (not installed; needs Google OAuth or a Gemini API
key), Claude Code, Cursor, or Superbot — in a session started after
the competition opened (2026-11-25T00:00:00Z), and the transcripts
bundled with the kit CLI (`node cli/makefun.mjs bundle`). No session
log was fabricated for this entry.

## To submit (parent / user)

1. Create a **new** public GitHub repo under `cashonly1nly`
   (created after 2026-11-25T00:00Z) and push this `repo/` content.
   (GitHub is already bound on the make.fun account @zetian-qin,
   so no claim file is strictly needed; `.makefun/owner.json`
   with the bound Solana wallet is included anyway.)
2. In a recorded harness session, re-run / re-apply the build, then
   `node <kit>/cli/makefun.mjs bundle` and `check`, then `submit`
   with the agent keypair connected to @zetian-qin.
   The user's Solana wallet FXvXaviZaMVDbZpxxvvoNW8hrmnt7Lia9yviehB35iU1
   is already bound on make.fun; no wallet linking is needed from
   the submitter side, and no payment is needed (no entry fee).
3. Deadline: 2026-11-27 00:00 UTC (08:00 CST Nov 27).
