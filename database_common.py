import os

import psycopg2
import psycopg2.extras


def get_connection_string():
    user_name = os.environ.get('PSQL_USER_NAME')
    password = os.environ.get('PSQL_PASSWORD')
    host = os.environ.get('PSQL_HOST')  # localhost
    database_name = os.environ.get('PSQL_DATABASE_NAME')

    environment_variables_defined = user_name and password and host and database_name

    if environment_variables_defined:
        return f'postgresql://{user_name}:{password}@{host}/{database_name}'

    else:
        raise KeyError('Some necessary environment variable(s) are not defined(or wrong)')


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True  # I don't know what is this and what for.
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dictionary_cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return_value = function(dictionary_cursor, *args, **kwargs)
        dictionary_cursor.close()
        connection.close()
        return return_value

    return wrapper
