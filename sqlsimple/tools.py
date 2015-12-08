from collections import OrderedDict
from sys import argv
import argparse

from sqlsimple.configuration import CONFIGURATION


def sqlsimple():
    commands = OrderedDict([
        ('help', help_text),
        ('init', init),
        ('init-db', init_db),
        ('make-migration', make_migration),
    ])
    if len(argv) == 1:
        return help_text(commands, [])
    command, args = argv[1], argv[2:]
    if command == 'help':
        return help_text(commands, args)
    elif command not in commands:
        print('{c} is not a valid sqlsimple command'.format(c=command))
        print()
        return help_text(commands)
    else:
        return commands[command](args)


def help_text(commands, args):
    if len(args) > 0 and args[0] in commands:
        commands[args[0]].help_text()
        return

    if len(args) > 0 and args[0] not in commands:
        print('{c} is not a valid sqlsimple command'.format(c=args[0]))

    print('Available commands are:')
    for command in commands.keys():
        print('  - {c}'.format(c=command))
    print()
    print('Use `sqlsimple <command> --help` for more detailed help')


class SqlSimpleCommand(object):
    parser = argparse.ArgumentParser()

    def help_text(self):
        self.parser.print_help()


class InitDb(SqlSimpleCommand):
    def __init__(self):
        self.parser.add_argument('database')

    def __call__(self):
        with open('schema.sql') as f:
            sql = f.read()
        return sql_exec(sql)


init_db = InitDb()


def init(args):
    pass


def make_migration(args):
    pass
