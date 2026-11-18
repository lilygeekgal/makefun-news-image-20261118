# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lilygeekgal/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/lilygeekgal/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

This entry sums up the world's news of Wednesday 18 November 2026 in a single image: a newspaper front page carrying the day's biggest stories. The image is stored in this repository as `entry.png`, and `main.py` is the program that delivers it. When run, `main.py` copies `entry.png` byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png` when that variable is not set), creating the output directory first if needed. It uses only the Python standard library, makes no network requests, and produces identical bytes on every run.

## Verify

Run it twice into two different output directories and compare the results:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.png /tmp/out2/entry.png
```

Both hashes must match, and both must match the hash of `entry.png` in this repository. The image itself is a 1024x1024 PNG under 1 MiB.
