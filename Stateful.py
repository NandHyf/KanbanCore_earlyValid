import Alt, WithSqlite
import tomlkit

# uid related

# Toml Methods
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


# ----- Transit Command Handler -----
def Handler(app_commands):
    dbType = app_commands[-1]
    dbPath = app_commands[-2]
    # [todo 3] 检查dbPath是否对应dbType, 否的话报错并exit()

    exec_commands = app_commands[0:-2]

    if dbType == "sqlite3":
        WithSqlite.Regular(dbPath, exec_commands)


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


# ----- Docker related -----



if __name__ == "__main__":
    
    a_c = ['/', 'test.db', 'sqlite3']
    a_c1 = ['add', 'board', 'testBoardName', 'test.db', 'sqlite3']
    a_c2 = ['edit', 'board', 't_boardName', 'to', 't_newBoardName', 'test.db', 'sqlite3']
    e_c = ['add', 'board']

    # Operate_sqlite3("test.db", a_c1)
    Handler(a_c2)
