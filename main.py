#!/usr/bin/env python
def run():

    from lib import librarySetup
    from lib import databaseSetup
    from lib import shell
    from lib import uptime
    librarySetup.checkLibraries() #Check and install libraries
    databaseSetup.main() #Create database

    shell.permissions()

    from lib import setup
    #from lib import online
    import os

    if not os.path.isfile('.env'): #Initial setup
        setup.environment()
    setup.subdirectories()
    
    os.system("python3 lib/bot.py") #Run main program
run()
