# db_connection.py

import psycopg2


DATABASE_CONFIG = {
    'host': 'server',
    'database': 'postgres',
    'user': 'postgres',
    'port': 3306
}


def connect_db(database):
    if database != DATABASE_CONFIG['database']:
        raise ValueError("Couldn't not find DB with given name")
    conn = psycopg2.connect(host=DATABASE_CONFIG['host'],
                            user=DATABASE_CONFIG['user'],
                            database=DATABASE_CONFIG['database'])
    return conn
