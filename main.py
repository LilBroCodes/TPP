import tcc

reader = tcc.TppReader()
code = reader.open_tpp("main.tpp")
variables = []

for line in code:
    if "=" in line:
        name, data = reader.get_set(line)
        variables.append({
            "name": name,
            "data": data
        })

    if "(" in line:
        func = reader.check_function(line)
        if func:
            print(reader.check_args(line))


print(variables)
