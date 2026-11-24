// A working news-image-daily entry (Node 22, standard library only): its image is the entry.png beside this file, and
// the program copies it to /output/entry.png. A starting point, not a winner: replace the image. The gate takes a
// whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

// News-image entry generator for make.fun competition (23 November 2026)
// Automatically copies the generated 1024x1024 front-page entry.png to the output directory.

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const srcImage = new URL('./entry.png', import.meta.url);
const destImage = join(outputDir, 'entry.png');

try {
  if (!existsSync(outputDir)) {
    mkdirSync(outputDir, { recursive: true });
  }
  copyFileSync(srcImage, destImage);
  
  const stats = statSync(destImage);
  const maxSizeBytes = 1048576; // 1 MiB
  if (stats.size > maxSizeBytes) {
    console.error(`[news-image] Error: Image size ${stats.size} bytes exceeds 1 MiB limit!`);
    process.exit(1);
  }
  
  console.log(`[news-image] Successfully published front-page entry to ${destImage} (${stats.size} bytes)`);
} catch (error) {
  console.error('[news-image] Failed to copy entry image:', error);
  process.exit(1);
}


