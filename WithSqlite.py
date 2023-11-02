import sqlite3


# [todo 0]
# 1. 检查commands[5]是否为dbPath, 不是话报错(syntax error)
# ↑↑↑ 但是总感觉输入检查应该放在Controller里面(也就是放在前端去检查)...
# 前端检查语法, 冲突代回到后端去检查, 然后顺便就执行了
# 2. 命令里面的<KB>, <CL>, <EV>都代入检查是否存在, 区分add/edit(INSERT INTO/UPDATE)
# 3. 匹配SQL关键字
# 4. 拼完以后进行to和in的判断
# 5. 按正确的顺序拼SQL语句
# 6. 执行
dbPath = "dev.db"


def Exec_one(dbPath, commands):
    con = sqlite3.connect(dbPath)
    cur = con.cursor()

    cur.execute(commands)
    con.commit()
    re = cur.fetchall()
    con.close()

    return re


def Exec_many():
    pass
        

def IsExist(exec_commands, returnBool=True):
    tableName = str(exec_commands[1]).capitalize()

    ItemName = str(exec_commands[2])

    sqls = "SELECT name FROM {table} WHERE name='{name}'".format(table=tableName, name=ItemName)
    ie = Exec_one(dbPath, sqls)

    if ie != [] and returnBool == False:
        return ie
    
    elif ie != [] and returnBool == True:
        return True

    elif ie == []:
        return False
    
    else:
        # Alt.Err(errCode)
        print("err <Code>: unexpected error in existence check")


# [todo 4]
def Secondary_response():
    pass


class Sqls():
    objType = ""
    
    def select():
        # DISTINCT
        sqls = "SELECT FROM {table}".format(table=tableName)

    def add():
        pass

    def delete():
        pass

    def edit():
        pass

    def move():
        pass

    def bp():
        pass

    def home():
        pass


# Regular Start
def Regular(dbPath, exec_commands):
    
    # try:
        ie = IsExist(exec_commands)
        print("is exist: ", ie)
        tableName = str(exec_commands[1]).capitalize()
        # to的情况待处理
        itemName = str(exec_commands[2])
        exec_flag = False

        if ie == True:
            pass

        elif ie == False:
            pass

        elif exec_flag == True:
            # 有个数据库锁定的异常待处理(Multi-user)
            Exec_one(dbPath, sqls)

if __name__ == "__main__":

    while(1):
        sy_i = input("sql: ").split(" ")
        Regular(dbPath, sy_i)