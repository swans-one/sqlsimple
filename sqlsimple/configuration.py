from importlib import import_module
import configparser
import os


def get_and_parse_config():
    """Read configuration from sqlsimple config files.

    - sqlsimple.cfg
    - databases.cfg
    """
    db_config_location = os.environ.get('SQLSIMPLEDATABASES', 'databases.cfg')
    db_config = configparser.ConfigParser()
    db_config.read(db_config_location)
    config_dict = {
        'databases': {},
    }
    for db_name, config in db_config.items():
        config_dict['databases'][db_name] = {
            'engine': config.get('engine', 'sqlite3'),
            'database': config.get('name'),
            'user': config.get('user'),
            'password': config.get('password'),
            'host': config.get('host'),
            'port': config.get('port'),
        }
        db_dict = config_dict['databases'][db_name]
        try:
            db_dict['db_api_module'] = import_module(db_dict['engine'])
        except ImportError:
            msg = ('Engine: "{e}" in config for database "{db}"'
                   ' is not an installed module.')
            raise ImportError(msg.format(e=db_dict['engine'], db=db_name))
    return config_dict


CONFIGURATION = {}
_CONFIGURATION_LOADED = False


if not _CONFIGURATION_LOADED:
    CONFIGURATION = get_and_parse_config()
