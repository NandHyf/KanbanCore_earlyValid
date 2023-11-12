import Alt
import tomlkit, sqlite3

# uid related

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


def IsExist(tableName:str, itemName:str, returnBool:bool=True):
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
  

class objBoard():
    pass

class objClass():
    pass

class objEvent():
    pass


# 把config里面的DB config写成对象?
def BuildObj():
    pass


def GenModel():# Controller里面还有一个一样的方法
    # model IE?
    # over write?
    # exec
    pass

#      ↓ 'OC' == 'Operating Cursor'
class OC():
    def __init__(self, currentPath:list, previousPath:list, dbType:str, dbPath:str, tableName:str, columnName:str, newColumnName:str) -> None:
        self.cp = currentPath
        self.pp = previousPath

        self.dt = dbType
        self.dp = dbPath

        self.table = tableName
        self.name = columnName
        self.newName = newColumnName


    def select(self, aliveOnly:bool=True):# KAO, what about unclassified...
        if aliveOnly == True:
            # →                                                                                    ↓不对啊这样的话分不出来事件的分类了
            sqls = "SELECT name FROM {table} WHERE name='{name}' AND status='alive' or status='unclassified';".format(table=self.table, name=self.name)
        elif aliveOnly == False:
            sqls = "SELECT name FROM {table} WHERE name='{name}';".format(table=self.table, name=self.name)

        res = Exec_one(self.dp, sqls)

        # 也许需要一个后处理res = [('a'),('b')]这样的格式问题
        return res


    def add(self, addType:str="board", addName:str="", after_to:str=""):
        if addType == "board":
            ie = IsExist("Board", addName)

            if ie == True:
                print("err <Code>: Board already exist")

            elif ie == False:
                sqls = "INSERT INTO Board VALUES(null, '{name}', 'alive');".format(name=self.name)
    
        elif addType == "class":
            # 1. 检查cl存在
            ie = IsExist("Class", addName)

            # 2. 有没有指定目标(after_to)
            if ie == False:

                if after_to == "" and len(self.cp) == 1:
                    print("err <Code>: syntax error")

                elif 
                            
                

            elif ie == True:
                pass
            # 3. 没有指定目标的 情况下, 当前路径(dp)有没有可以输入的; 没有就err

        elif addType == "event":
            pass
 

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
            print("err <Code>: syntax error")
        
        elif moveObj == "CL":
            pass
        
        elif moveObj == "EV":
            pass      
        

    def back(self, backType, backPath=""):
        if backType == "home":
            sqls = "SELECT name FROM sqlite_master WHERE type='table' AND name is NOT 'sqlite_sequence';"

        elif backType == "previous":
            sqls = "SELECT name FROM {table} WHERE name='{}'"

        Exec_one(dbPath, sqls)


def Handler():
    pass


if __name__ == "__main__":
    dbPath = "dev.db"
