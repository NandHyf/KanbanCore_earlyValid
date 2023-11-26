from Controller import kbc_config
import Alt
import tomlkit, sqlite3


# ----- Operating Cursor -----
oc = {
    "dt":str, 
    "dp":str, 
    "cp":str, 
    "pp":str, 
    "tp":str, 
    "tp_in":str, 
    "tp_to":str, 
    "tp_attr":str
    }
# thoughts:
# class oc():
#   def get_oc(), def move_oc()


# ----- Toml Methods -----
def GetTomlDoc(tomlName:str):
    try:
        with open(tomlName, "rb") as t:
            doc = tomlkit.load(t)

            if doc == {}:
                input("error 0: could not found correct config file") 
                exit()

            return doc
        
    except:
        input("error 0: could not found correct config file") 
        exit()
    

def MatchTomlKey(tomlName:str, key:str, table:str="none") -> str:
    doc = GetTomlDoc(tomlName)

    if table == "none":
        return str(doc.item(key))
    
    elif table != "none":
        d = doc.unwrap()
        return str(d[table][key])


# no differernt between ↑ MatchTomlKey() ↑ except receives and returns in list
def MatchTomlKeys(tomlName:str, keys:list, table:str="none") -> list:
    doc = GetTomlDoc(tomlName)

    if table == "none":
        # rl == 'r'eturn 'l'ist
        rl = []

        for key in keys:
            try:
                rl.append(doc.item(key))
            except:
                pass

        return rl
    

    elif table != "none":
        rl = []
        d = doc.unwrap()

        for key in keys:
            try:
                rl.append(d[table][key])
            except:
                pass

        return rl
    

def MatchTomlTable(tomlName:str, tableName:str, returnType:str="list"):
    d = GetTomlDoc(tomlName).unwrap()

    if returnType == "list":
        return list(d.get(tableName).values())
    
    elif returnType == "dict":
        return d
    

# ----- Sqlite Methods -----
def Exec_one(dbPath:str, commands:list):
    con = sqlite3.connect(dbPath)
    cur = con.cursor()

    cur.execute(commands)
    con.commit()
    re = cur.fetchall()
    cur.close()
    con.close()

    return re


def IsExist(dbPath:str, tableName:str, itemName:str, returnBool:bool=True):
    # [todo 4] 这里面的.capitalize()后面需要根据config.toml里面的内容判断
    # 可能也不用, 因为KBCLEV的表名和本身并无关系
    tableName = tableName.capitalize()

    sqls = "SELECT name FROM {table} WHERE name='{name}'".format(table=tableName, name=itemName)
    ie = Exec_one(dbPath, sqls)

    if ie != [] and returnBool == False:
        return ie
    
    elif ie != [] and returnBool == True:
        return True

    elif ie == []:
        return False
    
    else:
        # Alt.Err(errCode)
        print("err <Code>: unexpected error in existence check")


# ----- Record_main(DB record as a class) -----
class RM():
    def __init__(self, type:str, name:str, dscrp:str, creator:str, relatedBoard:str, relatedClass:str, status:int) -> None:
        self.id = "null"
        self.type = type
        self.name = name
        self.dscrp = dscrp
        self.creator = creator
        self.createdTime = "datetime('now')"
        self.relatedBoard = relatedBoard
        self.relatedClass = relatedClass
        self.status = status

    
    def select():
        pass

    def add():
        pass

    def delete():
        pass

    def edit():
        pass

    def move():
        pass

    def back():
        pass

    def export():
        pass


# ----- Record_log_action(DB record as a class) -----
class RLA():
    pass


def GenModel():
    # model IE?
    # over write?
    # exec
    pass


# ----- Interactions Handler(with other .py) -----
def Handler():
    pass


if __name__ == "__main__":
    pass
