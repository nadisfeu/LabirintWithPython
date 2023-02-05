from funcoes import Funcoes
from funcoes import busca


file_path = 'C:/01 eu/02_programação/LabirintWithPython/Anexo/maze/maze3_blocks.txt'
f = Funcoes(file_path)
f.print_file()
print("**********************")
f.make_graph()
print(f.graph)
print("**********************")
print(f.start)
print(f.end)
print(busca(f.graph, f.start, f.end))
f.close_file()
