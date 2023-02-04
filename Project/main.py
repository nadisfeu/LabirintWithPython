from funcoes import Funcoes

file_path = r'Anexo/maze/maze3.txt'
f = Funcoes(file_path)
f.print_file()
for i in f.txt_to_matriz():
    print(i)
print("**********************")
f.make_graph()
print(f.graph)
f.close_file()
