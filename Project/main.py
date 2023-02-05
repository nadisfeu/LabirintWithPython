from funcoes import Funcoes
from funcoes import busca


file_path =  'C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/LabirintWithPython/Anexo/maze/toy.txt'
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
