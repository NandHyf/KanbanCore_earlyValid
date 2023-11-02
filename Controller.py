import Alt, Stateful
import datetime
    

# 如果需要再封装class Board/KB_Class/Event的话就在这里
class Client():

    def get_config():
        # [todo 4]
        configs = ['DBType', 'DBPath', 'lang', 'listStyle', 'displayTimeZone']
        # rl == 'r'eturn 'l'ist
        rl = Stateful.MatchTomlKeys("dev_config.toml", configs)
        
        global lang, listStyle, dbType, dbPath, displayTimeZone, currentPath
        dbType = rl[0]
        dbPath = rl[1]
        lang = rl[2]
        listStyle = rl[3]
        displayTimeZone = rl[4]
        currentPath = ""


    # [todo 4]
    def get_help():
        print(Stateful.MatchTomlKey("clean_config.toml", lang, "command-help"))


    # [todo 3]
    def InUTC(timeZone=0):
        dt_now_UTC0 = str(datetime.datetime.now(datetime.timezone.utc))
        return(dt_now_UTC0)
    

    # [todo 2]
    # 前端只检查输入数量正确, 内容正确统一代回后端检查
    def InputCheck(inputs):
        pass
              

    def TransitCommand():
        # do while or for (1)
        while(1):
            app_commands = input(currentPath + "/: ", ).split(" ")
            # Input exception check
            
            # [todo 1]
            # Client.InputCheck(app_commands)
            if len(app_commands) < 5:
                # Add CurrentPath && DBType && Path
                app_commands.append(currentPath)
                app_commands.append(dbPath)
                app_commands.append(dbType)

                Stateful.Handler(app_commands)

            elif len(app_commands) >= 5:
                print("app_commands >5 error")


    # [todo 4]
    def start():
        # 1. get config
        Client.get_config()

        # 2.
        startState = Stateful.Handler(['/', dbPath, dbType])
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