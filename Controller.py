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
        displayTimeZone = rl[4]

    def get_help():
        print(Stateful.matchTomlKey("clean_config.toml", lang, "command-help"))


    # not finished
    def InUTC(timeZone=0):
        dt_now_UTC0 = str(datetime.datetime.now(datetime.timezone.utc))
        return(dt_now_UTC0)
    

    def TransitCommand():
        # do while or for (1)
        while(1):
            app_commands = input(currentPath + "/: ", ).split(" ")
            # Input exception check
            
            # Add DBType && Path
            app_commands.append(dbPath)
            app_commands.append(dbType)
            Stateful.PackHandler(app_commands)


    def start():
        # 1. get config
        Client.get_config()

        global currentPath
        currentPath = " "
        # ↓↓↓ test code here ↓↓↓


        # ↑↑↑ test code here ↑↑↑

        # 2. Normalized Start Process
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