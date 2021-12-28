import database
def settings(message, guild_id):
    prefix = database.read_database("command_prefix", guild_id) #Gets the prefix for the guild
    if "help" in message.lower(): #Checks to see if the user is asking for help
        setting_list = ["minecraft_server [URL of Server]", "server_port [Server Port]", "command_prefix [Bot Prefix ('?' by default)", "map [URL of online map]", "download [World download link]"]
        msg = "Use the setting function to change settings of this bot for your server "
        msg = msg + "\nUse the following commands to change the settings"
        for i in setting_list: #Builds the help message from the help list
            msg = "{}\n - {}settings {}".format(msg, prefix, i) 
        return msg #Return back to bot.py
    splitMessage = message.split()
    try:
        command = str(splitMessage[0]) #Gets the command used as a baseline
        database.modify_database(splitMessage[(splitMessage.index(command)) + 1], splitMessage[(splitMessage.index(command)) + 2], guild_id)
        msg = "{} has been set to {}".format((splitMessage[(splitMessage.index(command)) + 1]), (splitMessage[(splitMessage.index(command)) + 2]))
    except:
        return "Not an available setting, use '{}settings help' for help".format(prefix)
    return msg