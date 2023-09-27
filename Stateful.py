# @author:hyf
import os
import base64, datetime
import tomlkit, sqlite3


class Trigger():
    def __init__(self, T_obj) -> None:
        self.T_obj = T_obj

    def generate_uid(T_obj):
        dt_now = str(datetime.datetime.now(datetime.timezone.utc))
        genText = str.encode(T_obj + "_" + dt_now)
        uid = base64.b64encode(genText)
        
        return(uid)


# ----- Methods binding command to model -----
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