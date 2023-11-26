# from Controller import kbc_config
import Alt
import tomlkit, sqlite3


# ----- Operating Cursor -----
oc = {
    "dt":str, 
    "dp":str,

    "cp":list, 
    "pp":list,

    "next_move":str,

    "tp":list, 
    "tp_in":list, 
    "tp_to":list, 
    "tp_attr":str
    }
# some thoughts:
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
    def __init__(self, type:str="", name:str="", dscrp:str="", creator:str="", relatedBoard:str="", relatedClass:str="", status:int=10) -> None:
        self.id = "null"
        self.type = type
        self.name = name
        self.dscrp = dscrp
        self.creator = creator
        self.createdTime = "datetime('now')"
        self.relatedBoard = relatedBoard
        self.relatedClass = relatedClass
        self.status = status

    
    def select(self, selectColumn:str="name", aliveOnly:bool=True):
        if aliveOnly == True:
            sqls = "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}' AND status={s.status};".format(sc=selectColumn, s=self)
        elif aliveOnly == False:
            sqls = "SELECT {sc} FROM compact_main WHERE type='{s.type}' AND name='{s.name}' AND realatedBoard='{s.relatedBoard}' AND relatedClass='{s.relatedClass}';".format(sc=selectColumn, s=self)
        
        return sqls


    def add(self, addColumn:str="compact_main"):
        sqls = "INSERT INTO {ac} VALUES({a.id}, '{a.type}', '{a.name}', '{a.dscrp}', '{a.creator}', '{a.createdTime}', '{a.relatedBoard}', '{a.relatedClass}', {a.status});".format(ac=addColumn, a=self)

        return sqls


    def delete(self): # 1. withStatus:int=10? 2. withConditions >= or > or <?
        sqls = "UPDATE compact_main SET status=-10 WHERE type='{d.type}' AND name='{d.name}' AND relatedBoard='{d.relatedBoard}' AND relatedClass='{d.relatedClass}';".format(d=self)

        return sqls

    def edit(self):
        pass

    def move(self):
        pass

    def back(self):
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
    asd = RM("board", "KB", "", "n.HE", "", "", )
    print(asd.select())
    input("hold: ")
