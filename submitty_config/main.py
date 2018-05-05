#!/usr/bin/env python3

from argparse import ArgumentParser, PARSER, RawDescriptionHelpFormatter
from . import __VERSION__


class SubcommandHelpFormatter(RawDescriptionHelpFormatter):
    def _format_action(self, action):
        # noinspection PyUnresolvedReferences,PyProtectedMember
        parts = super()._format_action(action)
        if action.nargs == PARSER:
            parts = "\n".join(parts.split("\n")[1:])
        return parts


def lint():
    pass


def create():
    pass


def parse_args():
    parser = ArgumentParser(formatter_class=SubcommandHelpFormatter)
    parser.add_argument('--version', action='version', version='%(prog)s ' + __VERSION__)
    subparser = parser.add_subparsers(metavar='command', dest='command')
    lint_parser = subparser.add_parser('lint', help='lint a config file')
    lint_parser.add_argument('file', help='path to config file to lint')
    create_parser = subparser.add_parser('create', help='create a config file')
    create_parser.add_argument('file', help='path to write config file to')
    return parser.parse_args()


def run():
    args = parse_args()
    if args.command == 'lint':
        lint()
    elif args.command == 'create':
        create()
    print(args)

