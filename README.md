# Minecraft Discord Version 3.1.1
Welcome to my GitHub

This is a Discord bot that is hosted publicly, it can tell you the status of your (or any public) Minecraft server and lists the players online.

#### Please note: This bot is for usage with multiple servers. If you want your own personal bot that you can customise please use [Minecraft Bot](https://github.coventry.ac.uk/hollan84/MinecraftDiscord) instead, as there is already a custom file that gets generated automatically 

#### Existing bots:
* [Stable](http://minecraftbot.alastairserver.co.uk/)
* [Development](http://minecraftbotdev.alastairserver.co.uk/)

## Table of Contents  
* [Running The Bot](#running-the-bot)
    * [Prerequisites](#prerequisites)
    * [Server Settings](#server-settings)
    * [Hardware](#hardware) 
* [Set Up Bot](#setting-up-the-discord-bot)  
* [Add Bot To Server](#inviting-your-bot)   

## Running the bot
To run this bot, just start __run.py__ in Python3 <br/><br/>
To change settings in this bot, run __configure.py__ in Python3<br/>
You _don't_ need to run __configure.py__ on the first run as there is a first time setup.  

### Prerequisites
You need __*Python 3.5.9*__+ and a stable internet connection in order to run this bot. 
When the code is run, it should automatically install the following libraries using pip3:
* mcstatus
* status
* dotenv
* googletrans
* discord.py <br/>
  
If this doesn't happen, please report it as an issue and install them manually. pip3 should automatically install if you don't already have it.

### Server Settings
Make sure you have your server properties set to __enable-query=true__ so that you can get the server information

### Hardware
You can run this bot on just about any hardware that can run Python but if you don't have a device that can keep this bot hosted 24/7, I would recommend using a [Raspberry Pi](https://www.raspberrypi.org/). They run Linux, are low cost, use very little power and are capable of running this code without an issue.

## Setting up the Discord bot

1) Go to the [Discord developer site](https://discordapp.com/developers/applications)

2) Click the "New Application" button<br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_create_app_button.png)

3) Give the application a name and click “Create”<br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_create_app_form.png)

4) Create a Bot User by navigating to the “Bot” tab and clicking “Add Bot”.<br/>
5) Click “Yes, do it!” to continue.<br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_create_bot_user.png)

6) Make sure that Public Bot is ticked if you want others to invite your bot.<br/>
7) You should also make sure that Require OAuth2 Code Grant is unchecked unless you are developing a service that needs it. If you’re unsure, then leave it unchecked.<br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_bot_user_options.png)
8) Copy the token using the “Copy” button.

#### Warning: It should be worth noting that this token is essentially your bot’s password. You should never share this to someone else. In doing so, someone can log in to your bot and do malicious things, such as leaving servers, ban all members inside a server, or pinging everyone maliciously.
#### The possibilities are endless, so do not share this token.

#### If you accidentally leaked your token, click the “Regenerate” button as soon as possible. This revokes your old token and re-generates a new one. Now you need to use the new token to login.

## Inviting the bot

1) Following from the previous steps, go to the OAuth2 tab<br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2.png)

2) Tick the “bot” checkbox under “scopes”. <br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2_scope.png)

3) Set the permissions required for the bot. For this Minecraft bot we only need the following permissions:
* Send Messages
* Manage Messages
* Embed Links
* Attach Files
* Read Message History <br/>
You can set as many permissions as you'd like which may be needed if you want to add your own code to this bot. <br/>
![New Application](https://discordpy.readthedocs.io/en/latest/_images/discord_oauth2_perms.png)

4) Now the resulting URL can be used to add your bot to a server. Copy and paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.
