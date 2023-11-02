import sqlite3
import Stateful

deType = "sqlite3"
dbPath = "dev.db"


# [todo 1]
# 1. 检查commands[5]是否为dbPath, 不是话报错(syntax error)
# ↑↑↑ 但是总感觉输入检查应该放在Controller里面(也就是放在前端去检查)...
# 前端检查语法, 冲突代回到后端去检查, 然后顺便就执行了
# 2. 命令里面的<KB>, <CL>, <EV>都代入检查是否存在, 区分add/edit(INSERT INTO/UPDATE)
# 3. 匹配SQL关键字
# 4. 拼完以后进行to和in的判断
# 5. 按正确的顺序拼SQL语句
# 6. 执行


class Op_sqlite3():
    def __init__(self, commands) -> None:
        self.dbPath = dbPath
        self.commands = commands
        self.tableName = str(commands[1]).capitalize()
        self.columnName = str(commands[2])
        # "to" condition need a "if"
        self.ItemName = str(commands[])
    

    def Exec(self):
        con = sqlite3.connect(dbPath)
        cur = con.cursor()

        cur.execute(self.commands)
        con.commit()
        re = cur.fetchall()
        con.close()

        return re
        

    def IsExist(self, returnBool=True):
        sqls = "SELECT {coumn} FROM {table} WHERE name='{name}'".format(column=self.columnName, table=self.tableName, name=self.ItemName)
        ie = Op_sqlite3.Exec(sqls)

        if ie != None and returnBool == False:
            return ie
        
        elif ie != None and returnBool == True:
            return True

        elif ie == None:
            return False
        
        else:
            print("unexpected processing error")


    def Secondary_response(self):
        pass

    # Regular Start
    def Regular(self):
        try:
            ie = Op_sqlite3.IsExist()

            if ie != None:
                Op_sqlite3.Exec(dbPath, sy_i)

        except:
            print("not exist")


if __name__ == "__main__":

    while(1):
        sy_i = input("sql: ").split(" ")
        Op_sqlite3.Regular(dbPath, sy_i)

        