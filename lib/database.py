import sqlite3
from sqlite3 import Error
import os

def database_read(sql):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()

def database_write(sql):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def devs(user):
    sql = '''SELECT username
            FROM developers'''
    for i in database_read(sql):
        user_value = i[0]
        if str(user) in str(user_value):
            return True
    return False

def permission_check(command, user):
    sql = '''SELECT {}
            FROM developers
            WHERE username = "{}"'''.format(command, user)
    for i in database_read(sql):
        user_value = i[0]
        if str(user_value) == "1":
            return True
    return False

def devs_read(table):
    sql = '''SELECT *
            FROM {}'''.format(table)
    return str(database_read(sql))

def add_dev(username):
    sql = '''INSERT INTO developers(username, data, deploy, add_dev, modify_dev, remove_dev, restart, start, stop)
            VALUES("{}", FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)'''.format(username)
    database_write(sql)

def remove_dev(username):
    sql = '''DELETE FROM developers
            WHERE username = "{}"'''.format(username)
    database_write(sql)

def modify_dev(username, permission, value):
    if value == "true":
        value = 1
    else:
        value = 0
    sql = '''UPDATE developers
            SET {} = "{}"
            WHERE username = "{}"'''.format(permission, value, username)
    database_write(sql)

def sql_guard(message):
    danger_commands = ["drop", "table", "delete", "from", "update", "insert",  "into", "select", "truncate"]
    for i in danger_commands:
        if i in message:
            return False
    return True

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def modify_database(header_name, change, guild_id):
    sql = '''UPDATE servers
            SET {} = "{}"
            WHERE guild_id = "{}"'''.format(header_name, change, guild_id)
    database_write(sql)

def add_player(player, nick):
    if read_player(player) == "":
        sql = '''INSERT INTO players(username, nickname)
                VALUES("{}","{}")'''.format(player, nick)
    else:
        sql = '''UPDATE players
                SET nickname = "{}"
                WHERE username = "{}"'''.format(nick, player)
    database_write(sql)

def read_player(player):
    sql = '''SELECT nickname
            FROM players
            WHERE username == "{}"'''.format(player)
    data = database_read(sql)
    if data:
        data = data[0]
        if data[0]:
            return data[0]
    return ""

def read_database(header_name, guild_id):
    sql = '''SELECT {}
            FROM servers
            WHERE guild_id == {}'''.format(header_name, guild_id)
    data = database_read(sql)
    if data:
        data = data[0]
        if data[0]:
            return data[0]
    return ""

def get_total(header_name):
    sql = '''SELECT {}
            FROM servers'''.format(header_name)
    return len(database_read(sql))

def insert_new_guild(conn, sql_vars):
    sql = '''INSERT INTO servers(guild_id, guild_name, server_port, command_prefix, antispam, language)
            VALUES(?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, sql_vars)
    return cur.lastrowid

def connect():
    database = os.path.dirname(os.path.realpath("database/db.db"))
    database = database + "/db.db"
    return create_connection(database)    

def new_guild(guild_id, guild_name):
    guild_id = (guild_id, guild_name, "25565", "?", "TRUE", "en")
    try:
        conn = conn
    except:
        conn = connect()

    if conn is not None: 
        print(insert_new_guild(conn, guild_id))

        conn.commit()

def guild_check(guild):
    try:
        conn = conn
    except:
        conn = connect()

    if conn is not None: 
        cur = conn.cursor()
        cur.execute("SELECT guild_id FROM servers WHERE guild_id = ?", (guild,))
        data = cur.fetchall()
        if len(data)==0:
            return False
        else:
            return True