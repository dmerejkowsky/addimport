import os
import click


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
def main(lang, text, file):
    click.echo(f"Adding {text} to {lang} {file}")
