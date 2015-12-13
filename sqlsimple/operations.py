# TODO: Accept parameters! In all of these functions
from sqlsimple.utils import run_sql_query, run_sql_exec


def sql_query(query, db='default'):
    return run_sql_query(sql, db)


def sql_query_file(query_name=None, filename=None, db='default'):
    pass


def sql_exec(sql, db='default'):
    return run_sql_exec(sql, db)


def sql_exec_many(sql, db='default'):
    pass


def sql_exec_file(exec_name=None, filename=None, db='default'):
    pass
