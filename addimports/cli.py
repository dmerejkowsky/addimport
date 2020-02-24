import os
import sys
import click

from .adder import Adder


def message(s):
    with open("/tmp/addimports.log", "a") as f:
        f.write(s + "\n")


class File(click.ParamType):
    name = "file"

    def convert(self, value, param, ctx):
        if not os.path.exists(value):
            self.fail(f"'{value}' does not exist")
        return value


@click.command()
@click.option("--lang", required=True, type=click.Choice(["c", "cpp", "go", "python"]))
@click.argument("file", type=File())
@click.argument("text")
def main(*, file, text, lang):
    message(f"Adding {text} to {lang} {file}")
    with open(file, "r") as f:
        source = f.read()
    adder = Adder(source, lang=lang)
    res = adder.add_import(text)
    with open(file, "w") as f:
        f.write(res)
