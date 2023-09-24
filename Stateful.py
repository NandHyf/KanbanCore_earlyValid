# @author:hyf
import sqlite3, tomlkit

# -----
class UserCommand:
    def __init__(self, obj, command) -> None:
        self.focusMode = False
        self.obj = obj
        self.command = command


    def app_help():
        pass


    def app_exit():
        exit()


    def app_export(self):
        pass

    
    def list_board(self):
        pass
    

    def list_event(self):
        pass


    def select_board(self):
        print(self.obj + "is selected")
        self.focusMode = True


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


class Trigger():
    def __init__(self) -> None:
        pass


class Board(UserCommand):
    def __init__(self) -> None:
        super().__init__()


class Event(UserCommand):
    def __init__(self) -> None:
        super().__init__()


# ----- functions binding command to model -----
class WithToml(UserCommand):
    def __init__(self, obj, command):
        super().__init__(obj, command)


class WithSqlite3(UserCommand):
    def __init__(self, obj, command):
        super().__init__(obj, command)
    

    def add_insert():
        pass

    def edit_update():
        pass

    def del_delete():
        pass


# class WithMd():

# class WithCsv():

# class WithMysql():