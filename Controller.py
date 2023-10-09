# @author: nandHyf

import Stateful, View

class Command():
    pass

class Client():

    def get_config():
        # T-B-C...
        configs = ['lang', 'listStyle']
        # rl == 'r'eturn 'l'ist
        rl = Stateful.matchTomlKeys("config.toml", configs)
        
        global lang, listStyle
        lang = rl[0]
        listStyle = rl[1]


    def get_help():
        print(Stateful.matchTomlKey("config.toml", lang, "command-help"))


    def start():
        # 1. get config
        Client.get_config()

        # test code
        Client.get_help()


        # 2. list board
        # Command.list

        # 3. wait command input
        command = input()


if __name__ == "__main__":
    Client.start()