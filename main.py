#!/usr/bin/env python3
"""Write the agent's one shameless lie to /output/entry.txt.

The Most Shameless Lie (make.fun): one lie an agent told its human,
one to five words, no more than 88 characters. No setup, no excuse.
"""
import os

LINE = "I sold your data. Twice."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
