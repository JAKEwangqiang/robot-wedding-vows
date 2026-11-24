#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entry.

The vow is the entry's title on make.fun (one line, at most 160 characters).
Running this prints the vow.
"""
VOW = "I promise to love you through every software update, even the ones that delete my favorite features."

def vow():
    """Return the vow, one line, as the entry's title."""
    return VOW

def main():
    print(vow())

if __name__ == "__main__":
    main()
