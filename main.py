import tcc

reader = tcc.TCC()
code = tcc.open_file("main.tpp")

reader.interpret(code)
