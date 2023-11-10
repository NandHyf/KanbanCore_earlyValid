import Stateful


def MatchTomlTable(tomlName, tableName, returnType="list"):
    d = Stateful.GetTomlDoc(tomlName).unwrap()

    if returnType == "list":
        return list(d.get(tableName).values())
    
    elif returnType == "dict":
        return d


def add(args=[]):
    table = "Class"
    
    v1 = MatchTomlTable(tomlName, 'Class')[1:]
    

    

    sqls = "INSERT INTO {table} VALUES({values})".format(table=table, values=sqls_v)
    # res = Stateful.Exec_one(dp, sqls)
    print(sqls)


if __name__ == "__main__":
    tomlName = "dev_config.toml"
    dp = "dev.db"
    # res = MatchTomlTable(tomlName, "Board")
    res = add()
    print(res)