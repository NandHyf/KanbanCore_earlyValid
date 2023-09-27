# @author: nandHyf

import os
# import Stateful
import tomlkit, sqlite3
import base64, datetime


class client():
    def __init__(self) -> None:
        pass

    def get_config():
        pass

    def excute():
        pass

    def start():
        pass


class User:
    def __init__(self, command, obj0=[], tag0=None, content=[], tag1=None, obj1=None) -> None:
        self.enableGlobalCommand = False
        self.command = command
        self.obj0 = obj0
        self.tag0 = tag0
        self.content = content
        self.tag1 = tag1
        self.obj1 = obj1


    def command_help():
        pass
        # try:
        #     with open("help.txt","r") as help:
        #         helpText = help.read()
        #         if helpText == '':
        #             print("could not find correct'help.txt'")
        #         else:
        #           print(helpText)
        # except:
        #     print("could not find correct'help.txt'")


    # def command_exit():
    #     exit()


    def command_export():
        pass

    
    def list_board():
        pass
    

    def list_event():
        pass


    def select_board():
        pass


    def Command_add():
        pass


    def Command_edit():
        pass


    def Command_move():
        pass


    def Command_delete():
        pass


    def Command_archive():
        pass


    def Command_back2home():
        pass


    def Command_get_info():
        pass
    

    def Command_get_num():
        pass


class Board(User):
    pass


class Event(User):
    pass


class Trigger():
    def __init__(self, T_obj) -> None:
        self.T_obj = T_obj


    def generate_uid(T_obj):
        dt_now = str(datetime.datetime.now(datetime.timezone.utc))
        genText = str.encode(T_obj + "_" + dt_now)
        uid = base64.b64encode(genText)
        
        return(uid)


# ----- functions binding command to model -----
class WithTxt():
    pass
    
class WithToml():
    pass

class WithSqlite3():
    def __init__():
        pass    

    
    def list_():
        pass
    
    def add_insert():
        pass

    def edit_update():
        pass

    def del_delete():
        pass
    
    con = sqlite3.connect("KanbanCore.db")
    cur = con.cursor

# class WithMd():


# class WithCsv():


# class WithMongo():


if __name__ == "__main__":
    
    command = input()