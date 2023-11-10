import Stateful


def MatchTomlTable(tomlName, tableName, returnType="list"):
    d = Stateful.GetTomlDoc(tomlName).unwrap()

    if returnType == "list":
        return list(d.get(tableName).values())
    
    elif returnType == "dict":
        return d


def add():
    values = []

    sqls = "INSERT INTO {table} VALUES({values})".format(table=self.table, values=values)
    res = Stateful.Exec_one(dp, sqls)


if __name__ == "__main__":
    tomlName = "dev_config.toml"
    dp = "dev.db"
    res = MatchTomlTable(tomlName, "Board")
    print(res)