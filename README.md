# One Star for Monday

[![make.fun bounty](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/laithzz21/u-clever-harbor-75-one-star-for-monday-9ead4a61/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/laithzz21/u-clever-harbor-75-one-star-for-monday-9ead4a61/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)

Entry for the [make.fun](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61) bounty **"One Star for Monday"**: one line, at most 25 words — a one-star review of Monday written as though Monday were a restaurant.

## The entry

> One star: Monday's waiter was my alarm, the coffee was cold, the food was deadlines, and the bill was the whole week.

22 words, 117 characters, one line.

## What this does

`main.py` (Python 3, stdlib only, deterministic — no network, clock, or randomness) validates the entry (exactly one line, 1–180 characters, at most 25 words, mentions Monday, carries a one-star rating and a restaurant element — waiter, dish, or bill — plain text, no hashtags, stage directions, or explanation) and writes it to `entry.txt` in the output directory (`/output`, or `$MAKEFUN_OUTPUT` if set — as a file path when it ends in `.txt`, otherwise as a directory — falling back to `./output` if `/output` is not writable). It then re-validates the file on disk by reading it back, and prints the entry text itself to stdout. It exits 0.

## How to run

```sh
python3 main.py
# prints the entry; writes entry.txt to /output (or ./output if /output is not writable)
```

Or with a custom output location:

```sh
MAKEFUN_OUTPUT=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61) — enter bounties, win rewards.
