""" this file deals with all user input """

import argparse
import os
#relative import. means "from this files package import data"
from . import data

def main():
    args = parse_args()
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser(description='GTI Command Line Interface')

    # Add subcommands
    commands = parser.add_subparsers(dest='command')
    commands.required = True

    # init subcommand
    init_parser = commands.add_parser('init', help='Initialize GTI repository')
    init_parser.set_defaults(func=init)

    return parser.parse_args()


def init(args):
    data.init()
    print(f"Initialized empty GTI repository in '{os.getcwd()}/{data.GTI_DIR}' directory.")


