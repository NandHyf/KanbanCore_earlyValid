import sqlite3
import Stateful

deType = "sqlite3"
dbPath = "dev.db"


def is_exist(tableName, columnName):
    pass

def Secondary_response():
    pass


def Operate_sqlite3(dbPath, commands):
    #                 0       1       2     3      4     5     6
    # commands e.g.['add', 'board', 'KB4']
    # commands e.g.['add', 'class', 'CL1', 'to', 'KB4']
    # commands e.g.['add', 'event', 'EV1', 'to', 'KB4', '/', 'CL2']
    # commands e.g.['add', 'event', 'EV2', 'to', 'KB4/CL3']

    v = "SELECT * FROM {tableName} WHERE name={name}".format(tableName=str(commands[1]).capitalize(), name="'"+commands[2]+"'")
    
    # sqls = ""

    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    # 1. exist check
    try:
        res = cur.execute(v)
        con.commit()
        print("res: ", res.fetchone() is None)

        # syntax right but not exist:
        if res.fetchone() is None == True:
            print("err <Code>: could not found, creat? y/n")
            # Secondary_response()
        # 2. exec command
        matched = Stateful.MatchTomlKeys('dev_config.toml', commands, 'sqlite3')
        print(matched)

    except:
        print("err <Code>: Syntax error")

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
        sy_i = input("sql: ").split(" ")
        Operate_sqlite3(dbPath, sy_i)