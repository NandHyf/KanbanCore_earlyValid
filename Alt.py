# ----- Pre notes
# err 0: correct config not found
# err 1: correct DB not found
# -----
import Stateful
import datetime, base64

def Err(errCode, lang):
    pass
    errText = ""
    input("error ", errCode, errText)
    exit()
