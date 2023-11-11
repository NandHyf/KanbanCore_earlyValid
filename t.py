import Stateful


def MatchTomlTable(tomlName, tableName, returnType="list"):
    d = Stateful.GetTomlDoc(tomlName).unwrap()

    if returnType == "list":
        return list(d.get(tableName).values())
    
    elif returnType == "dict":
        return d

# [todo 4] rebuild
def add(cp, addType, contents):
    if addType == "board":
        sqls = "INSERT INTO Board VALUES(null, '{name}', 'alive');".format(name=self.name)
        
    
    elif addType == "class":
        sqls = "INSERT INTO Class VALUES(null, '{name}', )"

    elif addType == "event":
        pass


    sqls = ""


    Stateful.Exec_one(dp, sqls)


if __name__ == "__main__":
    tomlName = "dev_config.toml"
    dp = "dev.db"
    # res = MatchTomlTable(tomlName, "Board")
    contents = []
    cp = ""
    res = add(cp, "class", )