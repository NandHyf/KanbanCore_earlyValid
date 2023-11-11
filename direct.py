import sqlite3
import Stateful

def Operate_sqlite3(dbPath, commands):

    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    # 1. exist check
    try:
        res = cur.execute(commands)
        con.commit()
        print("res.fetchone() is None: ", res.fetchone() is None)

        # syntax right but not exist:
        if res.fetchone() is None == True:
            print("err <Code>: could not found, creat? y/n")


    except:
        print("err <Code>: Syntax error")

    con.close()


if __name__ == "__main__":
    # while(1):
        # syi = input("sql: ").split()
        # sy_i = input("sql: ")
        # Operate_sqlite3("dev.db", sy_i)

    data = [
    ('null', 'CL2', 'KB2', 'alive')
    ]

    sqls = ""
