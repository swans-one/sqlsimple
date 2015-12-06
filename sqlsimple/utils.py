from contextlib import contextmanager

from sqlsimple.configuration import CONFIGURATION


def run_sql_query(sql, db):
    pass


def run_sql_exec(sql, db):
    pass


@contextmanager
def get_cursor(db_config):
    # TODO: Think about caching this connection and just using context
    # managers differently.
    possible_connection_params = [
        'database', 'user', 'password', 'host', 'port'
    ]
    kwargs = {k, db_config[k]
              for k in possible_connection_params
              if db_config[k] is not None}
    connection = db_config['db_api_module'].connect(**kwargs)
    cursor = connection.cursor()
    try:

        # Context managager body
        yield cursor

        connection.commit()
    except:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
