# @author:hyf

import base64, datetime
import tomlkit, sqlite3

# kw == 'k'ey 'w'ord; dt_now = date&&time in UTC
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
                input("Error 0: Could not find correct 'config.toml'")
                exit()

            return doc
        
    except:
        input("Error 0: Could not find correct 'config.toml'")
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
            rl.append(doc.item(key))

        return rl
    

    elif table != None:
        rl = []
        d = doc.unwrap()

        for key in keys:
            rl.append(d[table][key])

        return rl



# Sqlite3
def connect_sqlite3(dbPath):
    con = sqlite3.connect(dbPath)

    cur = con.cursor()

    cur.close()

def closeConnect():
    pass

def list_SELECT():
    pass

def add_CREATE():
    pass

def add_INSERT_INTO():
    pass

def edit_UPDATE():
    pass

def delete_DELELTE():
    pass

def delete_DROP():
    pass

# Markdown


# csv


# MongoDB