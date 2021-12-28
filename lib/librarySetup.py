def checkLibraries():

    import getpass
    import os

    '''Check to see if pip3 is installed'''
    try:
        os.system("pip3 -V")
    except:
        os.system("sudo apt install python3-pip")

    '''Check discord.py'''
    try:
        import discord
    except: 
        try:
            os.system("python3 -m pip install -U discord.py") #Linux/Mac OS
        except:
            os.system("py3 -m pip install -U discord.py") #Windows

    '''Check mcstatus'''
    try:
        import mcstatus
    except: 
        os.system("pip3 install mcstatus")

    '''Check status'''
    try:
        import status
    except:
        os.system("pip3 install status")

    '''Check dotenv'''
    try:
        import dotenv
    except:
        os.system("pip3 install python-dotenv")

    '''check google translate'''
    try:
        import googletrans
    except:
        os.system("pip3 install googletrans")

    

checkLibraries()