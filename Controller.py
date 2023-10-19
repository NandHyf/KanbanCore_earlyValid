import Exceptions
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

        global commands
        commands = []


    def get_help():
        print(Stateful.matchTomlKey("config.toml", lang, "command-help"))


    def TransitCommand():
        # current path as a var instead↓ of input text
        app_command = input("        ~/: ").split(" ")


        app_command.append(dbType)
        app_command.append(dbPath)
        Stateful.TransitHandler(app_command)


    def start():
        # 1. get config
        Client.get_config()

        # test code
        Client.TransitCommand()


        # 2. list board
        # Command.list


if __name__ == "__main__":
    Client.start()