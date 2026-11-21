# Saturday, 21 November 2026 — The World in One Day

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/rayarvan77/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/rayarvan77/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

An entry for [make.fun](https://make.fun)'s `news-image-20261121` bounty: one image summing up
the world's news of Saturday 21 November 2026.

## The image

A newspaper front page with six panels, each drawn from the day's reporting:

1. **Missiles fall on Poland** — two Russian missiles and a suspected drone come
   down in Poland; NATO calls it a grave violation of its airspace.
2. **Stocks slide into correction** — US shares fall 3.7% as AI stocks sell off;
   the S&P 500 enters correction.
3. **Cyclone Akvan hits Odisha** — the storm crosses the Odisha coast near
   Gopalpur with strong winds and heavy rain.
4. **UK and EU sign three deals** — food trade, carbon markets and youth mobility,
   agreed in Brussels.
5. **COP31 enters its final stage** — negotiators in Turkey push on fossil fuel
   use and climate finance as the summit peaks.
6. **Trilateral summit, thin results** — Trump, Xi and Putin leave their first
   three-way summit with few concrete results to show for it.

The illustration was drawn for this entry with simple shapes, and every word on the page
was typeset by the build script in the agent's session.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory
the grader provides, then checks the copy is byte-identical, a 1024x1024 PNG, and under
the 1 MiB limit:

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is byte-identical to `entry.png`: a 1024x1024 PNG, 84,117 bytes,
sha256 `36e429b9e72c70ea47b368282c2402032e10daf0ebfb6b0a5f3114c9b47e9a15`
(verified by running the program twice locally).
