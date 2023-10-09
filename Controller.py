# @author: nandHyf

import Stateful, View

class Command():
    pass

class Client():

    def get_config():
        # T-B-C...
        configs = ['lang', 'listStyle']
        rl = Stateful.matchTomlKeys("config.toml", configs)
        global lang, listStyle
        lang = rl[0]
        listStyle = rl[1]


    def get_help():
        print(Stateful.matchTomlKey("config.toml", lang, "command-help"))


    def excute():
        pass


    def start():
        # get config
        Client.get_config()

        # test code
        Client.get_help()


        # list board
        # Command.list

        # wait command input
        command = input()


if __name__ == "__main__":
    Client.start()