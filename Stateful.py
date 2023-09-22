# @author:hyf
class Command:
    def __init__(self, obj, command) -> None:
        self.focusMode = False
        self.obj = obj
        self.Command = command


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


class Board(Command):
    def __init__(self) -> None:
        super().__init__()


class Event(Command):
    def __init__(self) -> None:
        super().__init__()

# class WithMd():

# class WithCsv():

# class WithMysql():