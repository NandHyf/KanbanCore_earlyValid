import Alt
import tomlkit, sqlite3

# uid related

# ----- Toml Methods -----
def GetTomlDoc(tomlName):
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
    

def MatchTomlKey(tomlName, key, table=None) -> str:
    doc = GetTomlDoc(tomlName)

    if table == None:
        return str(doc.item(key))
    
    elif table != None:
        d = doc.unwrap()
        return str(d[table][key])


# no differernt between ↑ MatchTomlKey() ↑ except receives and returns in list
def MatchTomlKeys(tomlName, keys, table=None) -> list:
    doc = GetTomlDoc(tomlName)

    if table == None:
        # rl == 'r'eturn 'l'ist
        rl = []

        for key in keys:
            try:
                rl.append(doc.item(key))
            except:
                pass

        return rl
    

    elif table != None:
        rl = []
        d = doc.unwrap()

        for key in keys:
            try:
                rl.append(d[table][key])
            except:
                pass

        return rl
    

def MatchTomlTable(tomlName, tableName, returnType="list"):
    d = GetTomlDoc(tomlName).unwrap()

    if returnType == "list":
        return list(d.get(tableName).values())
    
    elif returnType == "dict":
        return d
    

# ----- Sqlite Methods -----
def Exec_one(dbPath, commands):
    con = sqlite3.connect(dbPath)
    cur = con.cursor()

    cur.execute(commands)
    con.commit()
    re = cur.fetchall()
    con.close()

    return re


def IsExist(exec_commands, returnBool=True):
    # [todo 4] 这里面的.capitalize()后面需要根据config.toml里面的内容判断
    # 可能也不用, 因为KBCLEV的表名和本身并无关系
    tableName = str(exec_commands[1]).capitalize()

    ItemName = str(exec_commands[2])

    sqls = "SELECT name FROM {table} WHERE name='{name}'".format(table=tableName, name=ItemName)
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
  

class objBoard():
    pass

class objClass():
    pass

class objEvent():
    pass


# 把config里面的DB config写成对象?
def BuildObj():
    pass


def GenModel():
    pass


class Command():
    def __init__(self, dbPath, tableName, columnName, newColumnName) -> None:
        self.dp = dbPath

        self.table = tableName
        self.name = columnName
        self.newName = newColumnName


    def select(self, aliveOnly=True):
        if aliveOnly == True:
            sqls = "SELECT name FROM {table} WHERE name='{name}' AND status='alive';".format(table=self.table, name=self.name)
        elif aliveOnly == False:
            sqls = "SELECT name FROM {table} WHERE name='{name}';".format(table=self.table, name=self.name)

        res = Exec_one(self.dp, sqls)

        # 也许需要一个后处理res = [('a'),('b')]这样的格式问题
        return res


    def add(self, values, addObj="board", addType="new"):
        # get values
        values = []
        # 
        sqls = "INSERT INTO {table} VALUES({values})".format(table=self.table, values=values)
        res = Exec_one(self.dp, sqls)


    def delete(self):
        sqls = "UPDATE {table} SET status='deleted' WHERE name='{name}';".format(table=self.table, name=self.name)
        res = Exec_one(self.dp, sqls)


    def edit(self):
        # 感觉应该调二级响应去做吧...

        # edit boardName

        # edit className

        # edit eventName

        # edit event dscrp

        # edit event blabla
        pass
        

    def move(self, moveObj):
        if moveObj == "KB":
            pass
        
        elif moveObj == "CL":
            pass
        
        elif moveObj == "EV":
            pass      
        

    def back(self, backType, backPath=""):
        if backType == "home":
            sqls = "SELECT name FROM sqlite_master WHERE type='table' AND name is NOT 'sqlite_sequence';"

        elif backType == "previous":
            sqls = ""

        Exec_one(dbPath, sqls)


def Handler():
    pass


if __name__ == "__main__":
    dbPath = "dev.db"
