import database
import os
import time
import sys
import broadcast

async def developer_modify(message):
    msg = ""
    command = message[1]
    command = command.lower()
    if command == "deploy":
        os.system("git pull")
        time.sleep(10)
        path = os.path.dirname(os.path.realpath("developer.py"))
        path = "{}{}".format(path.replace("lib/", "/"), "/run.py")
        print(path)
        os.execlp(path)
        exit()
    elif command == "start":
        start = True
        return "This is WIP and currently doesn't work"
    elif command == "restart":
        path = os.path.dirname(os.path.realpath("developer.py"))
        path = "{}{}".format(path.replace("lib/", "/"), "/run.py")
        print(path)
        os.execv(path, sys.argv)
    if len(message) >= 2:
        if command == "data":
            if message[2] == "*":
                for table_name in ["servers", "players", "developers"]:
                    msg = "{}  \n__________________\n_**{}**_\n__________________  \n{}".format(msg, table_name, database.devs_read(table_name))
                return msg
            elif "select" in message[2].lower():
                sql = "SELECT"
                for statement in range(3, len(message)):
                    sql = "{} {}".format(sql, message[statement])
                try:
                    return database.database_read(sql)
                except:
                    return "Invalid SQL"
            try:
                return database.devs_read(message[2])
            except:
                return "Invalid Command"
        elif command == "add_dev":
            if not database.devs(message[2]):
                database.add_dev(message[2])
                return "{} added as a developer".format(message[2])
            else:
                return "{} is already a developer".format(message[2])
        elif command == "remove_dev":
            if database.devs(message[2]):
                database.remove_dev(message[2])
                return "{} is no longer a developer".format(message[2])
            else:
                return "{} is not a developer at the moment".format(message[2])
        elif command == "broadcast":
            if len(message) == 2:
                return "Please add a message to broadcast"
            return "broadcast"
        elif command == "server_list":
            return "server_list"
        if len(message) >= 4:
            if command == "modify_dev":
                if database.devs(message[2]):
                    if message[4] == "true" or message[4] == "false":
                        database.modify_dev(message[2], message[3], message[4])
                        return "{} permissions have been set to {} for {}".format(message[3], message[4], message[2])
                    else:
                        return "Please spefify if you want this to be true or false"
                else:
                    return "{} is not a developer".format(message[2])
            else:
                return "Invalid command, see the developer help for info"
        else:
            return "Invalid command, see the developer help for info"
    else:
        return "You need a variable to change, see '?developer help' for more info"

async def check_message(message, author, guild_id):
    message = message.split()
    if len(message) == 1:
        return "Please specify a command, use '{}developers help' for help".format(database.read_database("command_prefix", guild_id))
    if message[1] == "help":
        dev_help = {
            "restart" : "Restart all bots",
            "deploy" : "Deploy the current code version to all bots and restart",
            "data [table]" : "Display all data associated with table",
            "add_dev [username]" : "Add Discord developer",
            "modify_dev [username] [permission] [true/false]": "Modify permission of a developer",
            "remove_dev [username]" : "Remove developer"
        }
        msg = ""
        for i in dev_help:
            fw = i.split()
            if fw[0] in message:
                return "{}{} - {}".format(database.read_database("command_prefix", guild_id), i, dev_help[i])
            msg = "{} - {}developers {}\n".format(msg, database.read_database("command_prefix", guild_id), i)
        msg = "{}You can use {}developers help [developer command] to get more information on that command".format(msg, database.read_database("command_prefix", guild_id))
        return msg
    if database.permission_check(message[1], author):
        return await developer_modify(message)

async def developer_check(message, author, guild_id):
    if database.devs(author):
        return await check_message(message, author, guild_id)
    else:
        return "You don't have developer permissions to use this"