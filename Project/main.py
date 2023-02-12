from funcoes import Funcoes
from funcoes import busca


arquivo = input("Digite o arquivo que deseja tertar:\nExemplo: " + "maze3\n").lower().replace(" ", "")
file_path = 'Anexo/maze/' + arquivo + '.txt'
f = Funcoes(file_path)
f.print_file()
print("**********************")
f.make_graph()
print(f.graph)
print("**********************")
print(f.start)
print(f.end)
print(f.print_coordinates_path())
print(busca(f.graph, f.start, f.end))
