import sqlite3
from sqlite3 import Error
import os

#from python_variables import * 

def create_initial_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def add_primary_developer(conn, username):
    from . import database
    if not database.devs(username):
        sql = '''INSERT INTO developers(username, data, deploy, add_dev, modify_dev, remove_dev, restart, start, stop, broadcast)
                VALUES("{}", TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE)'''.format(username)
        cur = conn.cursor()
        cur.execute(sql)
        return cur.lastrowid

def main():
    database_path = os.path.dirname(os.path.realpath("database/db.db"))
    database_path = "{}/db.db".format(database_path)

    create_server_table_sql = """CREATE TABLE IF NOT EXISTS servers ( 
                                guild_id integer PRIMARY KEY,
                                guild_name text,
                                minecraft_server text,
                                server_port integer,
                                command_prefix text,
                                map text,
                                download text,
                                antispam text,
                                language text
                            );"""
    create_player_table_sql = """CREATE TABLE IF NOT EXISTS players ( 
                                username text PRIMARY KEY,
                                nickname text
                            );"""

    create_dev_table_sql = """CREATE TABLE IF NOT EXISTS developers ( 
                                username text PRIMARY KEY,
                                data bool,
                                deploy bool,
                                add_dev bool,
                                modify_dev bool,
                                remove_dev bool,
                                restart bool,
                                start bool,
                                stop bool,
                                broadcast bool
                            );"""

    if not os.path.isfile(database_path):
        create_initial_connection(database_path)

    conn = create_connection(database_path)

    if conn is not None: 
        create_table(conn, create_server_table_sql)
        create_table(conn, create_player_table_sql)
        create_table(conn, create_dev_table_sql)

        add_primary_developer(conn, "AlastairHolland#6538")

    conn.commit()