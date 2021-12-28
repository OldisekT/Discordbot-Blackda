import os
import discord
import status
import datetime

from mcstatus import MinecraftServer
from datetime import datetime
from datetime import timedelta
from shutil import copyfile
from googletrans import Translator

import database
import settings
import developer
import bot_functions as functions

from python_variables import *

copyfile(".env", "lib/.env") #Copies the env file to the lib directory

from dotenv import load_dotenv
load_dotenv() #Loads the environment variable

token = os.environ['ODIyNDczMDU5NzI5NDA4MDQx.YFSxug.tGY-z8g0egzm0wKToO7kpLM1oZI'] #Loads the bot token
client = discord.Client() #Sets the client for Discord

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!') 
	status = "{} different servers".format(database.get_total("*")) #Gets the total number of servers that the bot has a database of
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status)) #Sets the status to how many servers the bot is tracking

@client.event
async def on_message(message):

	guild_id = str(hash(message.guild)) #Gets the numerical ID of the server

	if database.guild_check(guild_id) == False: #Checks to see if there is no record of the server that has just sent a message
		guild_name = str(message.guild) #Gets the name of the guild from the message
		database.new_guild(guild_id, guild_name) #Adds a blank guild to the servers database
		status = "{} different servers".format(database.get_total("*")) #Gets how many servers the bot has a record of
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status)) #Changes the status

	prefix = database.read_database("command_prefix", guild_id) #Reads the prefix that the server has set, ? by default

	if not message.content.startswith(prefix): #Checks to see if the message starts with the prefix
		return #No point checking the rest of the message if the message doesn't start with the prefix

	user_message = functions.language(message.content, guild_id) #Splits the message up to be read easier later
	message_command = user_message.split() 
	message_command = message_command[0] #Gets the command to be checked which increases speed of the checks

	server = MinecraftServer(database.read_database("minecraft_server", guild_id), int(database.read_database("server_port", guild_id))) #Read the minecraft database

	'''Checking which command has been issued'''
	if message.author == client.user: #Make sure that the bot doesn't reply to itself
		return
	elif ('help') in message_command:
		msg = functions.help(user_message, prefix, guild_id)
	elif ('source') in message_command:
		msg = "Self Hosted: {}\nHosted: {}".format(sites["custom_github"], sites["hosted_github"])
	elif ('share') in message_command:
		msg = "Add to other servers!\nNormal Bot: {}\nDeveloper Bot: {}\n(Don't add both bots to the same server due to command conflicts)".format(sites["normal_bot"], sites["developer_bot"])
	elif ('map') in message_command:
		msg = database.read_database("map", guild_id)
	elif ('server') in message_command:
		msg = database.read_database("minecraft_server", guild_id)
	elif ('download') in message_command:
		msg = database.read_database("download", guild_id)
	elif ('version') in message_command:
		msg = "Minecraft Bot - Version {}".format(str(os.environ['VERSION']))
	elif ('donate') in message_command:
		msg = "Donate to the development of this bot here:\n{}\nIf you want to be added to the donator list, add your Discord ID as a reference".format(sites["paypal"])
	elif ('support') in message_command:
		msg = "Join our support server here:\n{}".format(sites["support"])
	elif ('botinfo') in message_command:
		msg = "Minecraft Bot - Version {}\n".format(str(os.environ['VERSION']))
		msg = "{}Total Discord Servers: {}\n".format(msg, database.get_total("*"))
		msg = "{}{}\n".format(msg, functions.uptime())
		#msg = "{}Total Minecraft Servers: {}\n".format(msg, database.get_total("minecraft_server"))
		#msg = "{}Percentage of servers using maps: {}%\n".format(msg, str((int(database.get_total("map"))/int(database.get_total("minecraft_server"))*100)))
	elif ('uptime') in message_command:
		msg = functions.uptime()
	elif ('developer') in message_command:
		msg = await developer.developer_check(message.content, message.author, guild_id)
		if msg == "broadcast":
			m = message.content
			m = m.split()
			broadcast_message = ""
			for word in range(2, len(m)):
				broadcast_message = "{}{} ".format(broadcast_message, m[word])
			server_count = 0
			if broadcast_message == "remind ":
				broadcast_message = ""
			for server in client.guilds:
				server_sql = '''SELECT minecraft_server FROM servers WHERE guild_name = "{}"'''.format(server)
				server_data = database.database_read(server_sql)
				if len(server_data) > 0:
					server_data = server_data[0]
					server_data = server_data[0]
				for channel_list in server.channels:
					try:
						if server_data == "None" or server_data == None:
							await channel_list.send("{}\nYou haven't set your minecraft server yet, to do this use '{}settings help' to see which settings you are able to change on this bot".format(broadcast_message, prefix))
						else:
							await channel_list.send(broadcast_message)
						server_count += 1
						break
					except Exception:
						continue
					else:
						break
			msg = "'{}' has been sent to {} servers".format(broadcast_message, server_count)
		elif msg == "server_list":
			msg = ""
			for server in client.guilds:
				msg = "{}- {}\n".format(msg, server)
	elif ('status') in message_command:
		if not database.read_database("minecraft_server", guild_id) == None or not database.read_database("minecraft_server", guild_id) == "None":
			try:
				status = server.status()
				query = server.query()
				if status.players.online > 0:
					msg = str("The server has {0} players and replied in {1} ms\nPlayers:\n - {2}".format(status.players.online, status.latency, "\n - ".join(query.players.names)))
				else:
					msg = str("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
			except:
				try:
					server.status()
					msg = "{} is online".format(database.read_database("minecraft_server", guild_id))
				except:
					msg = "{} doesn't seem to be responding; please message {} for help".format(database.read_database("minecraft_server", guild_id), "the admins")
		else:
			msg = "The Minecraft server is not set, use '{}settings help' to see how to change this".format(prefix)
		checkNicknames = msg.split("\n - ")
		for player in checkNicknames:
			if len(database.read_player(player)) > 0:
				nick = "{} [{}]".format(player, database.read_player(player))
				msg = msg.replace(player, nick)
	elif ('settings') in message_command:
		if not database.sql_guard(message.content): #Checks to see if the message contains any words that could compromise data
			return #Don't respond if the message contains anything dangerous
		if "Minecraft Bot" in str(message.author.roles):
			msg = settings.settings(message.content, guild_id)
		else:
			msg = "You need to have the role 'Minecraft Bot' to change these settings"
	elif ('minecraftnickname') in message_command:
		if not database.sql_guard(user_message): #Checks to see if the message contains any words that could compromise data
			return #Don't respond if the message contains anything dangerous
		splitMessage = user_message.split() #Split the message into a list
		database.add_player(splitMessage[1], splitMessage[2])
		msg = "Set " + splitMessage[1] + "'s nickname to " + splitMessage[2]
	else: #If the message is blank
		msg = "That is not a valid command, use {}help for help\nIf this command conflicts with another bot, use '{}settings prefix [prefix]' to change it".format(prefix, prefix)

	if msg == None:
		msg = "This setting doesn't appear to be currently set, use {}settings to change this".format(prefix)
	
	channel = message.channel #Gets the channel of the message

	message_character_limit = 2000
	for index in range(0, len(msg), message_character_limit):
		await channel.send(msg[index:index+message_character_limit]) #Send the message

client.run(token)

