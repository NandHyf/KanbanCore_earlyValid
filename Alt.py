# ----- Pre notes
# err 0: correct config not found
# err 1: correct DB not found
# -----
import Stateful
import datetime, base64, uuid

def Err(errCode, lang='en'):
    errText = ""
    input("err ", errCode, ": ",  errText)
    exit()