import discord
import os

import database
import settings
import developer

from python_variables import *

from dotenv import load_dotenv
load_dotenv() #Loads the environment variable

token = os.environ['TOKEN'] #Loads the bot token
client = discord.Client() #Sets the client for Discord

@client.event
async def broadcast(msg):
    server_count = 0
    print(client.guilds)
    for server in client.guilds:
        for channel in server.channels:
            try:
                await client.send_message(channel, msg)
                server_count += 1
                break
            except Exception:
                continue
            else:
                break
    return str(server_count)

@client.event
async def on_ready():
    await client.start(token)