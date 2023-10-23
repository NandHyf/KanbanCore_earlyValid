import Alt
import Stateful


class Client():

    def get_config():
        # T-B-C...
        configs = ['lang', 'listStyle', 'DBType', 'DBPath']
        # rl == 'r'eturn 'l'ist
        rl = Stateful.matchTomlKeys("config.toml", configs)
        
        global lang, listStyle, dbType, dbPath
        lang = rl[0]
        listStyle = rl[1]
        dbType = rl[2]
        dbPath = rl[3]


    def get_help():
        print(Stateful.matchTomlKey("config.toml", lang, "command-help"))


    def TransitCommand():
        # do while or for (1)
        app_command = input(currentPath).split(" ")


        app_command.append(dbPath)
        app_command.append(dbType)
        Stateful.TransitHandler(app_command)


    def start():
        # 1. get config
        Client.get_config()

        global currentPath
        currentPath = "/: "
        # ↓↓↓ test code here ↓↓↓


        # ↑↑↑ test code here ↑↑↑

        # Normalized Start Process
        startState = Stateful.TransitHandler(['list', 'board', dbPath, dbType])
        
        Client.TransitCommand()


        # 2. list board
        # Command.list


if __name__ == "__main__":
    Client.start()