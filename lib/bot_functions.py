import database

from googletrans import Translator

from python_variables import *
from uptime import *

def help(user_message, prefix, guild_id):

	msg = "" #Sets a blank message to add to
	for command in commands: #Iterates through the list of commands
		if command in user_message: #Checks to see if the user is checking a specific command instead of the command list
			msg = "{}{} - {}".format(prefix, command, commands[command]) #Sets msg to the help for that specific command
	if len(msg) == 0: #Checks to see if msg has aleady been added to
		msg = "Commands:\n"
		for command in commands: #Iterates over the commands
			if command == "map" or command == "download": #Checks to see if the command to be listed is 'map' or 'download' (Removes 'map'/'download' if not set in settings)
				if database.read_database(command, guild_id) is not None: #If there is a value assocated with the value 'map' or 'download' in the guild record
					msg = "{}- {}{}\n".format(msg, prefix, command) #Add map or download to the msg
			else:
				msg = "{}- {}{}\n".format(msg, prefix, command) #Add command to the message
		msg = "{}If you want more information on a specific command use '{}help [command name]'".format(msg, prefix) #Additional help
	return msg

def language(user_message, guild_id):
	if database.read_database("language", guild_id) != "en": #If the server is not set as english
		translator = Translator()
		user_message = user_message[len(prefix):]
		user_message = translator.translate(user_message, src=database.read_database("language", guild_id), dest='en') #Translate the message to English
		user_message = "{}{}".format(prefix,user_message.text) #Rebuild message
	return user_message.lower() #Returns the lowercase message

def plural(int_value):
	if str(int_value) == "1":
		return ""
	return "s"

def uptime():
	curr_time = datetime.datetime.now()
	uptime = curr_time - start_time
	return "Bot Uptime: {} day{}, {} hour{}, {} minute{} and {} second{}".format(uptime.days, plural(uptime.days), (uptime.seconds//3600)%24, plural((uptime.seconds//3600)%24), (uptime.seconds//60)%60, plural((uptime.seconds//60)%60), uptime.seconds%60, plural(uptime.seconds%60))