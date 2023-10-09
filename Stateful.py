# @author:hyf
import os
import base64, datetime
import tomlkit, sqlite3

# kw == Key Word
# dt_now == date&&time in UTC
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
                print("Error 0: Could not find correct 'config.toml'")
                exit()

            return doc
        
    except:
        print("Error 0: Could not find correct 'config.toml'")
        exit()
    

def matchTomlKey(tomlName, key):
    doc = getTomlDoc(tomlName)
    return doc.item(key)
    

# Sqlite3
    

# Markdown


# csv


# MongoDB