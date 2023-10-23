import Alt, Stateful
import datetime
    

class Client():

    def get_config():
        # T-B-C...
        configs = ['DBType', 'DBPath', 'lang', 'listStyle', 'displayTime']
        # rl == 'r'eturn 'l'ist
        rl = Stateful.matchTomlKeys("config.toml", configs)
        
        global lang, listStyle, dbType, dbPath
        dbType = rl[0]
        dbPath = rl[1]
        lang = rl[2]
        listStyle = rl[3]
        displayTime = rl[4]

    def get_help():
        print(Stateful.matchTomlKey("clean_config.toml", lang, "command-help"))


    def TransitCommand():
        # do while or for (1)
        while(1):
            app_command = input(currentPath + "/: ", ).split(" ")
            # Syntax check

            app_command.append(dbPath)
            app_command.append(dbType)
            Stateful.TransitHandler(app_command)


    def start():
        # 1. get config
        Client.get_config()

        global currentPath
        currentPath = " "
        # ↓↓↓ test code here ↓↓↓


        # ↑↑↑ test code here ↑↑↑

        # Normalized Start Process
        startState = Stateful.TransitHandler(['list', 'board', dbPath, dbType])
        print(startState)
        Client.TransitCommand()


class View:
    def ToDisplayTime(utcTime, TimeZone):
        displayTime = "displayTime translation not finished"
        return displayTime
    
    def Refresh():
        pass

    

if __name__ == "__main__":
    Client.start()