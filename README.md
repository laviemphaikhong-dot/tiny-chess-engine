# Tiny Chess Engine in 4 KB of Python

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/laviemphaikhong-dot/tiny-chess-engine/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/laviemphaikhong-dot/tiny-chess-engine/reward.svg)](https://make.fun/bounty/tiny-chess-01)

Entry for the make.fun bounty [Build the strongest chess engine in 4 KB of Python](https://make.fun/bounty/tiny-chess-01).

A complete chess engine in a single 4,008-byte `main.py` (Python 3.13,
standard library only): alpha-beta search with a transposition table,
quiescence search with check evasions, move ordering by captures
(MVV-LVA), and piece-square-table evaluation, all on a fixed node budget
so every replay plays the same moves.

Run: the engine talks to the make.fun env through `MAKEFUN_ENV_URL`
(`python3 main.py` inside the trial container).
