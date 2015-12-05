import configparser
import os


def get_and_parse_config():
    db_config_location = os.environ.get('SQLSIMPLEDATABASES', 'databases.cfg')
    db_config = configparser.ConfigParser()
    db_config.read(db_config_location)
    config_dict = {
        'databases': {},
    }
    for db_name, config in db_config:
        config_dict['databases'][db_name] = {
            'engine': config.get('engine', 'sqlite3')
            'name': config.get('name')
            'user': config.get('user')
            'password': config.get('password')
            'host': config.get('host')
            'port': config.get('port')
        })
    return config_dict


CONFIGURATION = {}
_CONFIGURATION_LOADED = False


if not _CONFIGURATION_LOADED:
    CONFIGURATION = get_and_parse_config()
