import os
def environment():
    
    '''Prevents overwriting of the environment file'''
    settingList = ["Token"] #Only setting to change is the Token for this bot
    if os.path.isfile('.env'): #Checks to see if there is an environment file
        overwrite = input("Would you like to change your current settings? (y/n) > ")
        overwrite = overwrite.lower() #Makes the input string lowercase
        if overwrite == "y" or overwrite == "yes":
            print("\nChoose settings to change")
            for i in settingList:
                print("{} - {}".format((settingList.index(i)+1), i)) #Lists all the options to set
            settingsChoice = input("\nInput the numbers of the settings you want to change\nYou can change multiple numbers by typing more than one (Example: 12345)\n > ")
        else:
            return #Exit function
    else: #If the environment file has not been set
        settingsChoice = ""
        for s in range(1, len(settingList)+1): #Goes through all the options and selects all of them to set
            settingsChoice = settingsChoice + str(s)

    '''Gets information'''
    if str(settingList.index("Token")+1) in settingsChoice:
        token = input("Input your bot token here > ")
    else:
        token = os.environ['TOKEN']

    version = "3.0.0"

    data = "TOKEN={}\nVERSION={}".format(token,version) #Sets the format of the data

    '''Write data to the .env file'''
    creds = open(".env", "w")
    creds.write(data)
    creds.close()

    '''Verify the data has been written'''
    print("\nVerifying data..")
    verify = open(".env")
    readData = verify.read()
    verify.close()
    if data == readData:
        print("Data written successfully")
        return
    else:
        tryAgain = ("Error writing data. \n Try again? (y/n) > ")
        tryAgain = tryAgain.lower() #Makes the input string lowercase
        if tryAgain == "y" or tryAgain == "yes":
            environment()
        else:
            return

def subdirectories():
    if not os.path.isdir("database"):
        os.makedirs("database")