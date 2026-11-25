// news-image-20261125 entry (Node 22, standard library only).
// The image is entry.png beside this file, drawn by build_image.py from
// verified 25 November 2026 news (see NEWS_SOURCES.md). The program copies
// it to /output/entry.png, exactly as the kit's starter does.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const out = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(out, { recursive: true });
copyFileSync(
  new URL('./entry.png', import.meta.url),
  join(out, 'entry.png'),
);
