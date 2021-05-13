"""Console script for file_format_inspector."""
import sys
import click
from rich import print
import json
from file_format_inspector import inspect_jsonl


@click.command()
@click.option("--path", type=click.Path(exists=True), help="File to be inspected")
def main(path):
    """Automatically inspect the format of the file"""
    structure = inspect_jsonl(path)
    print(json.dumps(structure, indent=4))


if __name__ == "__main__":

    sys.exit(main())  # pragma: no cover
