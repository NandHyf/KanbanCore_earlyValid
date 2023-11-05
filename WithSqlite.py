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


# [todo 4]
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


class objBoard():
    def __init__(self, dbPath, previousPath, currentPath, boardName, newBoardName) -> None:
        self.dp = dbPath
        self.pp = previousPath
        self.cp = currentPath

        self.name = boardName
        self.newName = newBoardName


    def select_board(self, aliveOnly=True):# 不太对劲, 应该在IsExist的时候就已经可以得到结果了
        if aliveOnly == True:
            sqls = "SELECT name FROM Board WHERE name='{name}' AND status='alive';".format(name=self.name)
        elif aliveOnly == False:
            sqls = "SELECT name FROM Board WHERE name='{name}';".format(name=self.name)

        reserve = Exec_one(self.dp, sqls)
        # [todo 4]
        # return sqls


    def add_board(self):
        sqls = "INSERT INTO Board VALUES(null, '{name}', 'alive');".format(name=self.name)
        Exec_one(self.dp, sqls)
        

    def delete_board(self):
        sqls = "UPDATE Board SET status='deleted' WHERE name='{name}';".format(name=self.name)
        Exec_one(self.dp, sqls)
        

    def edit_board():
        # 修改了Board之后关联的分类和事件也要变, 而且要先修改关系最后变board名称
        # 1. 查找CL和EV里面和这个KB的关联
        # 2. 修改关联的KB-name
        # 3. 修改KB的name
        sqls = ""
        

    def move_board():
        print("err <Code>: syntax error")


class objClass():
    def __init__(self, dbPath, previousPath, currentPath, className, newClName="") -> None:
        self.dp = dbPath
        self.pp = previousPath
        self.cp = currentPath

        self.name = className
        self.newName = newClName


    def select_class(self, aliveOnly=True):# 不太对劲, 应该在IsExist的时候就已经可以得到结果了
        if aliveOnly == True:
            sqls = "SELECT name FROM Class WHERE name='{name}' AND status='alive';".format(name=self.name)
        elif aliveOnly == False:
            sqls = "SELECT name FROM Class WHERE name='{name}';".format(name=self.name)

        reserve = Exec_one(self.dp, sqls)
       

    def add_class(self):
        sqls = "INSERT INTO Class VALUES(null, '{name}', 'alive');".format(name=self.name)
        Exec_one(self.dp, sqls)
        

    def delete_class(self):
        sqls = "UPDATE Class SET status='deleted' WHERE name='{name}';".format(name=self.name)
        Exec_one(self.dp, sqls)
        # [todo 3] 关联的EV和KB待处理
        

    def edit_class(self):
        sqls = "UPDATE Class SET name={newName} WHERE name='{name}';".format(newName=self.newName, name=self.name)
        Exec_one(self.dp, sqls)


    def move_class(self):
        # Why would someone want to do that?
        # cp[todo 4] or del ONLY: def copy_class():
        print("err <Code>: syntax error")



class objEvent():
    def __init__(self, dbPath, previousPath, currentPath, eventName, newEventName, dscrp, newDscrp, classCreated, classCurrent) -> None:
        self.dp = dbPath
        self.pp = previousPath
        self.cp = currentPath

        self.name = eventName
        self.newName = newEventName
        self.dscrp = dscrp
        self.nd = newDscrp
        self.ccr = classCreated
        self.ccu = classCurrent
        
    def select_event(self):
        sqls = "SELECT * FROM Event WHERE name='{name}';".format(name=self.name)
        reserve = Exec_one(self.dp, sqls)


    def add_event(self):
        sqls = "INSERT INTO Event VALUES(null, '{name}', '{dscrp}', '{creator}', datetime('now'), '{classCreated}', '{classCurrent}', 'alive');"
        Exec_one(self.dp, sqls)


    def delete_event(self):
        sqls = "UPDATE Event SET status='deleted' WHERE name='{name}';".format(name=self.name)
        Exec_one(self.dp, sqls)


    def edit_event(self, target):
        # newName
        if target == "newName":
            sqls = "UPDATE Event SET name='{newName}' WHERE name='{name}';".format(newName=self.newName, name=self.name)
            # [todo 4] 更改之后自动跳转?

        # newDscrp && appendDscrp
        elif target == "newDscrp":
            sqls = "UPDATE Event SET dscrp='{newDscrp}' WHERE name='{name}';".format(newDscrp=self.nd, name=self.name)
            
        elif target == "appendDscrp":
            sqls = "SELECT dscrp FROM Event WHERE name='{name}'".format(name=self.name)
            reserve = Exec_one(self.dp, sqls)
            # some prosess
            sqls = reserve + ""

        Exec_one(self.dp, sqls)



    def move_event(self):
        sqls = "UPDATE Event SET classCurrent='{classCurrent}' WHERE name='{name}';".format(classCurrent=self.ccu, name=self.name)
        Exec_one(self.dp, sqls)


# [todo 3]
def bp():
    pass


def home(): # IE就能解决了好像
    sqls = "SELECT name FROM sqlite_master WHERE type='table' AND name is NOT 'sqlite_sequence';"
    Exec_one(dbPath, sqls)

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
            pass
            # 有个数据库锁定的异常待处理(Multi-user)
            # Exec_one(dbPath, sqls)

if __name__ == "__main__":

    while(1):
        sy_i = input("sql: ").split(" ")
        Regular(dbPath, sy_i)