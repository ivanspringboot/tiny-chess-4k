"""Replay short games and print the engine's move at 12 sampled positions.

Run from this directory with: python difftest.py
"""
import io
import os
import urllib.request

# engine.py starts its game loop at import time; make that loop exit immediately
# so the module can be imported for testing without a live MAKEFUN server.
os.environ.setdefault("MAKEFUN_ENV_URL", "http://localhost")
urllib.request.urlopen = lambda *args, **kwargs: io.BytesIO(b'{"status":"done"}')

import engine

START = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
PIECE = " PNBRQKpnbrqk"

GAMES = [
    ["e2e4", "e7e5", "g1f3", "b8c6", "f1b5", "a7a6", "b5a4", "g8f6"],
    ["d2d4", "d7d5", "c2c4", "e7e6", "b1c3", "g8f6", "c1g5", "f8e7"],
    ["e2e4", "c7c5", "g1f3", "d7d6", "d2d4", "c5d4", "f3d4", "g8f6"],
]


def to_fen():
    ranks = []
    for r in range(7, -1, -1):
        row = ""
        empty = 0
        for f in range(8):
            v = engine.h[r * 16 + f]
            if v:
                if empty:
                    row += str(empty)
                    empty = 0
                row += PIECE[v]
            else:
                empty += 1
        if empty:
            row += str(empty)
        ranks.append(row)
    cast = "".join(c for bit, c in ((1, "K"), (2, "Q"), (4, "k"), (8, "q")) if engine.u & bit) or "-"
    ep = "-" if not engine.o else "abcdefgh"[engine.o & 15] + str((engine.o >> 4) + 1)
    return "/".join(ranks) + " " + ("w" if engine.g == 0 else "b") + " " + cast + " " + ep + " 0 1"


def position_after(plies):
    engine.setup(START)
    for move in plies:
        encoded = engine.ba(move)
        if encoded not in engine.gen(engine.g):
            raise ValueError("illegal move " + move)
        engine.mk(encoded)
    return to_fen()


def legal_moves(fen):
    engine.setup(fen)
    return [engine.uci(n) for n in engine.gen(engine.g)]


def main():
    engine.init()
    cases = []
    for game in GAMES:
        for cut in (2, 4, 6, 8):
            cases.append(position_after(game[:cut]))
    assert len(cases) == 12
    for i, fen in enumerate(cases, 1):
        moves = legal_moves(fen)
        print("%2d %s -> %s" % (i, fen, engine.think(fen, moves)))


main()
