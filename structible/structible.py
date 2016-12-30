"""The structible submodule defines the commandline interface."""

import logging
import click


@click.group()
def cli():
    """Create and manage ansible project trees."""
    pass


@cli.command()
def init():
    """Create an empty ansible project tree."""
    pass


if __name__ == '__main__':
    cli()
