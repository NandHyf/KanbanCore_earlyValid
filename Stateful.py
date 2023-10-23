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


# ----- Methods binding command to model -----

# Toml
def getTomlDoc(tomlName):
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
    

def matchTomlKey(tomlName, key, table=None) -> str:
    doc = getTomlDoc(tomlName)

    if table == None:
        return str(doc.item(key))
    
    elif table != None:
        d = doc.unwrap()
        return str(d[table][key])


def matchTomlKeys(tomlName, keys, table=None) -> list:
    doc = getTomlDoc(tomlName)

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
            rl.append(d[table][key])

        return rl


# Sqlite3
def operate_sqlite3(dbPath, command):
    con = sqlite3.connect(dbPath)
    cur = con.cursor()

    # list -> .TABLES
    if command[0] == "list" and command[1] == "board":
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(cur.fetchall())
    # add -> CREATE
    elif command[0] == "add" and command[1] == "board":
        cur.execute('''        ''')

    # add -> INSERT INTO

    # edit -> UPDATE

    # delete -> UPDATE(status -> 'deleted')
    
    cur.close()


# Markdown


# csv


# MongoDB


# ----- Transit Command Handler -----
def TransitHandler(transit_command):
    dbType = transit_command[-1]
    dbPath = transit_command[-2]
    exec_command = transit_command[0:-2]

    if dbType == "sqlite3":
        operate_sqlite3(dbPath, exec_command)

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