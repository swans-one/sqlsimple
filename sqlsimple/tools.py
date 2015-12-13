from collections import OrderedDict
from sys import argv
import argparse

from sqlsimple.configuration import CONFIGURATION
from sqlsimple.operations import sql_exec


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
    """Base class for commands
    """
    def help_text(self):
        self.parser.print_help()


class InitDb(SqlSimpleCommand):
    """Initialize the database.

    - Run the statements in the schema
    - Load any fixtures
    - Set up the migrations table
    - Mark any migrations as run
    """
    # TODO: get the schema from the configuration
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', default='default', required=False)

    def __call__(self, args):
        args = vars(self.parser.parse_args(args))
        with open('schema.sql') as f:
            sql_script = f.read()
        ss = [s.strip() for s in sql_script.split(';') if s.strip() != '']
        for statement in ss:
            sql_exec(statement, db=args['database'])


class Init(SqlSimpleCommand):
    """Generate the structure of the project.

    - Create blank configuration files
      - databases.cfg
      - sqlsimple.cfg
    - Create schema.sql
    - Create migrations directory
    """
    parser = argparse.ArgumentParser()

    def __call__(self, args):
        pass


class MakeMigration(SqlSimpleCommand):
    """Setup blank files for a migration in the migration directory.

    - #####_name_forward.sql
    - #####_name_backward.sql
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('database')

    def __call__(self, args):
        pass


class Migrate(SqlSimpleCommand):
    """Run migrations
    """
    parser = argparse.ArgumentParser()

    def __call__(self, args):
        pass


# Initialize the callables used for these commands
init_db = InitDb()
init = Init()
make_migration = MakeMigration()
migrate = Migrate()
