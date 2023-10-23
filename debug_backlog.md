# ----- config.toml -----
1. DBPath 是否支持填写路径/绝对路径/相对路径: 第一版只支持当前目录吧, 后面再说其他目录和multi的情况

# ----- Controller.py -----
1. app_command 输入不合法字符的异常处理
2. 原本该在Focus模式工作的SELECT出现在全局命令里的异常处理

# ----- Stateful.py -----
1. 读取toml文件时候没有匹配到键的异常处理: 已解决(通过table=None的参数)
2. list board 之后返回None要不要做异常处理(成换行)
3. add命令的判断: 是CREATE 还是 INSERT INTO

# ----- Alt.py -----

# ----- Model -----
1. 不同类别命名既然相互引用了那其中一个看板的某个类别改了名称其他引用了该类型的也会被改了


# ----- Reference for dev -----
## list
> list board <boardName>

> list class <className> in <boardName>

> list event -> err <err_code>: # 或者说这里该是事件详情吗？（展开事件那种）

## add
> add board <boardName> 
CREATE TABLE <boardName>(<board_uid>, <board_name>, <status>);

> add class <className> to <boardName>
check_exist()
    exist:


    not-exist:
        INSERT INTO <Class> VALUES
        (<class_uid>, <class_name>, <used_board>, <status>)

> add event <eventName> to <boardName>/<className> # 草！超出去了，报个error算了(╬▔皿▔)╯
> (已经在某个事件下面) add event <eventName> to <className> # 淦已经看到重构的大坑了

> add event <eventName> -d <descriptions> # 中间带空格怎么办?

> add event <eventName> -ddl <ddlTime>

> add event <eventName> -d <descriptions> -ddl <ddlTime>


## edit
> edit board <boardName> to <newBoardName>
UPDATE 

> edit class <className> to <newClassName>
# 新建一个类别和引用关系, 然后再把旧的类别里面的引用关系删除
INSERT INTO <ClassTable> VALUES ()
UPDATE 

> edit event <eventName> in <boardName>


## delete


## move


## select


## ..


## /
> /
# 记得设置 currentPath = "/" 
"SELECT name FROM sqlite_master WHERE type='table';"