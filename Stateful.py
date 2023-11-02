import Alt
import uuid
import tomlkit, sqlite3

# Place for uid


# ----- Methods binding app command to model -----
# Toml
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


# Sqlite3
def Exist_in_sqlite3(tableName, columnName=None, recordName=None):
    if columnName == None:
        s = "SELECT name FROM sqlite_master WHERE type='table' AND name='{tableName}';".format(tableName = tableName)

    if columnName != None:
        s = "SELECT * FROM {tableName} WHERE {columnName}={recordName}".format(tableName = tableName, columnName = columnName, recordName = recordName)


def Operate_sqlite3(dbPath, match_commands):
    matchedSyntax = MatchTomlKeys("dev_config.toml", match_commands, "sqlite3")

    # 需要检查的类型
    # Board, 禁止重复
    # Class, 重复就update一个引用关系
    # Event, 同一个Board里面不允许重复, 不同Board里可以重复

    s = "".join(matchedSyntax).format(tableName = match_commands[1], objName = match_commands[2])
   

    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    
    # is_exist()
    res = cur.execute(s).fetchall()
    # ret = res.fetchall()
    # if res = None:
    

    con.close()
    return res


# Markdown


# csv


# MongoDB


# ----- Transit Command Handler -----
def Handler(app_commands):
    dbType = app_commands[-1]
    dbPath = app_commands[-2]

    if dbType == "sqlite3":
        # IsExist()
        # Operated_sqlite3()
        return Operate_sqlite3(dbPath, app_commands)

    elif dbType == "csv":
        pass

    elif dbType == "mongodb":
        pass

    elif dbType == "toml":
        pass

    elif dbType == "md":
        pass

    else:
        input("error 1: could not found correct Data Base")
        exit()


if __name__ == "__main__":
    
    a_c = ['/', 'test.db', 'sqlite3']
    a_c1 = ['add', 'board', 'testBoardName', 'test.db', 'sqlite3']
    a_c2 = ['edit', 'board', 't_boardName', 'to', 't_newBoardName', 'test.db', 'sqlite3']
    e_c = ['add', 'board']

    # Operate_sqlite3("test.db", a_c1)
    PackHandler(a_c2)
    