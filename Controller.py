# @author: nandHyf

import Stateful, View

class Command():
    pass

class Client():
    def __init__(self) -> None:
        pass


    def get_config():
        doc = Stateful.getTomlDoc("config.toml")
        
        # T-B-C...
        global lang
        lang = ""


    def get_help():
        t = Stateful.matchTomlKey("config.toml", "lang")
        print(t)


    def excute():
        pass


    def start():
        # get config
        Client.get_config()

        # test aera
        Client.get_help()

        # list board
        # Command.list

        # wait command input
        command = input()


if __name__ == "__main__":
    Client.start()