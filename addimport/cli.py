import argparse
import os
import sys

from .adder import Adder


def message(s):
    with open("/tmp/addimport.log", "a") as f:
        f.write(s + "\n")


def add_import(file, text, *, lang):
    if file == "-":
        source = sys.stdin.read()
    else:
        with open(file, "r") as f:
            source = f.read()
    adder = Adder(source, lang=lang)
    res = adder.add_import(text)
    if file == "-":
        sys.stdout.write(res)
    else:
        with open(file, "w") as f:
            f.write(res)


def main():
    message(f"sys.argv: {sys.argv}")
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", required=True, choices=["c", "cpp", "go", "python"])
    parser.add_argument("file")
    parser.add_argument("text")

    args = parser.parse_args()

    add_import(args.file, args.text, lang=args.lang)
