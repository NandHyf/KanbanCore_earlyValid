# @author: nandHyf

import Stateful, View

class Command():
    def list():
        pass

    def add():
        pass
    
    def delete():
        pass

    def edit():
        pass
    
    def move():
        pass

    def backHome():
        pass

    def backPrevious():
        pass
    


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


    def handleCommand():
        pass


    def start():
        # 1. get config
        Client.get_config()

        # test code



        # 2. list board
        # Command.list

        # 3. wait command input
        command = input()


if __name__ == "__main__":
    Client.start()