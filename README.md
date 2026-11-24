[![competition](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/xingxing717/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/xingxing717/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in One Day — Monday 23 November 2026

A one-page front page summing up the world's news of Monday 23 November 2026:
37 stories across 7 regions (Middle East, Europe, Asia, Africa, the Americas,
Markets & Tech, Sport & Culture), led by Kyiv's claim that its sea drones sank
the Russian corvette Merkury off Benghazi, Libya.

## How it works

`render.py` draws the whole page with Pillow (pure code, DejaVu fonts, no
network, no randomness, no timestamps), writing `entry.png` (1024x1024).
`main.ts` copies that image to the output directory the grader provides
(`$MAKEFUN_OUTPUT_DIR`, default `/output`).

## Run it

```sh
python3 render.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Two runs produce byte-identical output.
