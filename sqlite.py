import sqlite3
import Stateful

deType = "sqlite3"
dbPath = "dev.db"


def IsEixist(tableName, columnName):
    pass
    sqls = ""
    Operate_sqlite3()



def BackPrevious():
    pass
    previousPath = ""
    currentPath = ""


# [todo 3]
def Secondary_response():
    pass


def Operate_sqlite3(dbPath, commands):
    # Commands e.g.
    #    0       1       2      3      4      5     6
    # [add]
    # ['add', 'board', '<KB>']
    # ['add', 'class', '<CL>', 'to', '<KB>']
    # ['add', 'event', '<EV>', 'to', '<KB>', '/', '<CL>'] <- 这个应该报错
    # ['add', 'event', '<EV>', 'to', '<KB>/<CL>']

    # [edit]
    # ['edit', 'board', '<KB>', 'to', '<KB>']
    # ['edit', 'class', '<KB>', 'to', '<KB>']
    # ['edit', 'class', '<CL>', 'to', '<CL>']
    # ['edit', 'class', '<CL>', 'to', '<CL>']
    # ['edit', 'event', '<EV>', 'to', '<EV>']
    # ['edit', 'event', '<EV>', 'in', '<KB>', '/', '<CL>'] <- 这个应该报错
    # ['edit', 'event', '<EV>', 'in', '<KB>/<CL>']

    # [delete]
    # ['delete', 'board', '<KB>']
    # ['delete', 'class', '<CL>']
    # ['delete', 'event', '<EV>']
    # ['delete', 'event', '<EV>', 'in', '<KB>', '/', '<CL>'] <- 这个应该报错
    # ['delete', 'event', '<EV>', 'in', '<KB>/<CL>']

    # [move]
    # ['move', 'class', '<CL>', 'to', '<KB>']
    # ['move', 'event', '<EV>', 'to', '<KB>']
    # ['move', 'event', '<EV>', 'to', '<CL>']
    # ['move', 'event', '<EV>', 'in', '<KB>', '/', '<CL>'] <- 这个应该报错
    # ['move', 'event', '<EV>', 'in', '<KB>/<CL>']

    # [select]
    # ['select', 'board', '<KB>']
    # ['select', 'class', '<CL>']
    # ['select', 'event', '<EV>']
    # ['select', 'event', '<EV>', 'in', '<KB>', '/', '<CL>'] <- 这个应该报错
    # ['select', 'event', '<EV>', 'in', '<KB>/<CL>']

    # [..]

    # [/]
    
    # [todo 1]
    # 1. 检查commands[5]是否为dbPath, 不是话报错(syntax error)
    # ↑↑↑ 但是总感觉输入检查应该放在Controller里面(也就是放在前端去检查)...
    # 前端检查语法, 冲突代回到后端去检查, 然后顺便就执行了
    # 2. 命令里面的<KB>, <CL>, <EV>都代入检查是否存在, 区分add/edit(INSERT INTO/UPDATE)
    # 3. 匹配SQL关键字
    # 4. 拼完以后进行to和in的判断
    # 5. 按正确的顺序拼SQL语句
    # 6. 执行

    v = "SELECT * FROM {tableName} WHERE name={name}".format(tableName=str(commands[1]).capitalize(), name="'"+commands[2]+"'")
    
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

    while(1):
        sy_i = input("sql: ").split(" ")
        Operate_sqlite3(dbPath, sy_i)