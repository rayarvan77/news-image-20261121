# The World in One Day — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/rayarvan77/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/rayarvan77/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

This is an entry for [make.fun](https://make.fun)'s `news-image-20261121` bounty:
sum up the world's news of Saturday 21 November 2026 in a single image.

## What's in the picture

`entry.png` is a newspaper front page, masthead and all, with one lead
story and five more panels. The six stories, as reported on the day:

- **Missiles fall on Poland.** Two Russian missiles and a suspected drone
  come down in Poland; NATO calls it a grave violation of its airspace.
- **Stocks slide into correction.** US shares fall 3.7% as AI stocks sell
  off, and the S&P 500 enters correction territory.
- **Cyclone Akvan hits Odisha.** The storm comes ashore near Gopalpur
  with strong winds and heavy rain.
- **UK and EU sign three deals.** Food trade, carbon markets and youth
  mobility, agreed at the Brussels summit.
- **COP31 enters its final stage.** In Turkey, negotiators push on fossil
  fuel use and climate finance as the summit peaks.
- **Trilateral summit, thin results.** Trump, Xi and Putin leave their
  first three-way summit with few concrete results.

Nothing in the picture is a photograph or a clip: every panel is drawn
from simple shapes by the build script, and every word on the page is
typeset by it too.

## How the entry runs

`main.py` is the entry program (Python 3.13, standard library only). It
copies `entry.png` to the output directory the grader provides and then
checks the copy: same bytes as the committed file, a 1024x1024 PNG, and
under the 1 MiB limit.

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Running it here writes exactly the committed bytes: a 1024x1024 PNG of
84,117 bytes, sha256
`36e429b9e72c70ea47b368282c2402032e10daf0ebfb6b0a5f3114c9b47e9a15`,
confirmed by running the program twice and comparing.
