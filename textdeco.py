import levels
import time
import os
import sys


def red(text):
    return f"\033[91m{text}\033[0m"


def green(text):
    return f"\033[92m{text}\033[0m"


def yellow(text):
    return f"\033[93m{text}\033[0m"


def underline(text):
    return f"\033[4m{text}\033[0m"


def bold(text):
    return f"\033[1m{text}\033[0m"


def blk_terminal():
    print("\n" * 200)


print("="*100)
