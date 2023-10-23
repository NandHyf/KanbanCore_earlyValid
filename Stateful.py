import Alt
import base64, datetime
import tomlkit, sqlite3

# kw == 'k'ey 'w'ord; dt_now = date&&time in UTC
# Please consider adding more salt to prevent uid duplication(specially under multi-user use case)
def generate_uid(kw):
    dt_now = str(datetime.datetime.now(datetime.timezone.utc))
    genText = str.encode(kw + "_" + dt_now)
    uid = base64.b64encode(genText)
    
    return(uid)


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
def Operate_sqlite3(dbPath, match_commands):
    matchedSyntax = MatchTomlKeys("dev_config.toml", match_commands, "sqlite3")

    s = " ".join(matchedSyntax)

    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    
    con.close()


# Markdown


# csv


# MongoDB


# ----- Transit Command Handler -----
def PackHandler(app_commands):
    dbType = app_commands[-1]
    dbPath = app_commands[-2]

    if dbType == "sqlite3":
        Operate_sqlite3(dbPath, app_commands)

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
    
    a_c = ['add', 'board', 'testBoardName', 'test.db', 'sqlite3']
    a_c1 = ['edit', 'board', 't_boardName', 'to', 't_newBoardName', 'test.db', 'sqlite3']
    e_c = ['add', 'board']
    
    # Operate_sqlite3("test.db", a_c1)
    PackHandler(a_c)
    