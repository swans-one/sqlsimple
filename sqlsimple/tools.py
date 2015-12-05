from collections import OrderedDict
from sys import argv
import argparse

from sqlsimple.configuration import CONFIGURATION


def sqlsimple():
    commands = OrderedDict([
        ('help', help_text),
        ('init', init),
        ('update-db', update_db),
        ('make-migration', make_migration),
    ])
    if len(argv) == 1:
        return help_text(commands)
    command, args = argv[1], argv[2:]
    if command == 'help':
        return help_text(commands)
    elif command not in commands:
        print('{c} is not a valid sqlsimple command'.format(c=command))
        print()
        return help_text(commands)
    else:
        return commands[command](args)


def help_text(commands):
    print('Available commands are:')
    for command in commands.keys():
        print('  - sqlsimple {c}'.format(c=command))
    print()
    print('Use `sqlsimple <command> --help` for more detailed help')


def update_db(args):
    with open('schema.sql') as f:
        print(f.readlines())
    print(CONFIGURATION['databases']['default']['name'])


def init(args):
    pass


def make_migration(args):
    pass
