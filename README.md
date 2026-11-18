# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/ivanspringboot/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/ivanspringboot/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A Python chess engine that plays within make.fun's tiny-chess-01 rules: alpha-beta
search with a transposition table, killer moves, late move reductions and a quiescence
search. The shipped `main.py` is an LZMA-packed bundle that `makefun compress` builds
from `src/engine.py`, keeping the submitted program at or below the 4,096-byte (4 KB)
limit.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8000 python main.py
```

Make changes in `src/engine.py` and repack it — `main.py` is generated output, not the
place to edit.

## Licence

MIT. See [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
