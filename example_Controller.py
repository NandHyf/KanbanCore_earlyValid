import Stateful


class Command():
    def __init__(self, order, obj0=[], tag0=None, content=[], tag1=None, obj1=None) -> None:
        self.enableGlobalCommand = False
        self.order = order
        self.obj0 = obj0
        self.tag0 = tag0
        self.content = content
        self.tag1 = tag1
        self.obj1 = obj1

    def help():
        pass

    def exit():
        exit()

    def export():
        pass

    def list_board():
        pass
    
    def list_event():
        pass

    def select_board():
        pass

    def add():
        pass

    def edit():
        pass

    def move():
        pass

    def delete():
        pass

    def archive():
        pass

    def back2home():
        pass

    def get_info():
        pass
    
    def get_num():
        pass


class Board():
    pass

class Event():
    pass