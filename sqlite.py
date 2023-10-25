import sqlite3
import Stateful

deType = "sqlite3"
dbPath = "dev.db"


def is_exist(tablePath, name):
    pass


def Operate_sqlite3(dbPath, commands):
    #                 0       1       2     3      4     5     6
    # commands e.g.['add', 'board', 'KB4']
    # commands e.g.['add', 'class', 'CL1', 'to', 'KB4']
    # commands e.g.['add', 'event', 'EV1', 'to', 'KB4', '/', 'CL2']
    # commands e.g.['add', 'event', 'EV2', 'to', 'KB4/CL3']
    
    matched = []
    matched = Stateful.MatchTomlKeys(commands)
    sqls = ""

    # 1. exist check

    # 2. exec command


    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    res = cur.execute(sqls)
    con.commit()
    print("res: ", res.fetchone())


    con.close()


if __name__ == "__main__":
    sy = "CREATE TABLE Board(board_uid, board_name, status)"
    sy1 = "INSERT INTO Board VALUES('1', 'board1', 'live');"
    sy2 = "DROP TABLE test;"
    sy3 = "DROP TABLE Board"
    sy4 = "CREATE TABLE Board(uid, name, status)"
    sy5 = "INSERT INTO Board VALUES('1', 'KB1', 'live');"

    sy6 = ['add', 'board', 'KB1']

    while(1):
        sy_i = input("sql: ")
        Operate_sqlite3(dbPath, sy_i)