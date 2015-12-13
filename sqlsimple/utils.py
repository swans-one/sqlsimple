from collections import namedtuple
from contextlib import contextmanager

from sqlsimple.configuration import CONFIGURATION


def run_sql_query(sql, db):
    """Execute and return results for a query.
    """
    with get_cursor(db_config) as cur:
        cur.execute(sql)
        cols = [col[0] for col in cur.description]
        Result = namedtuple('Result', cols)
        results = map(Result._make, cur.fetchall())
    return results


def run_sql_exec(sql, db):
    """Execute a sql statement, but do not return results from a query.
    """
    with get_cursor(db_config) as c:
        results = c.execute(sql)
    return results


@contextmanager
def get_cursor(db='default'):
    """Get a cursor object for a configured database, handle commit/rollback.
    """
    db_config = CONFIGURATION['databases'][db]
    # TODO: Think about caching this connection and just using context
    # managers differently.
    possible_connection_params = [
        'database', 'user', 'password', 'host', 'port'
    ]
    kwargs = {k: db_config[k]
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


def file_contents(exec_name=None, filename=None):
    """Get the sql query contained in a file.

    Search in sql directories to find sql files and cache the results.
    """
    pass
