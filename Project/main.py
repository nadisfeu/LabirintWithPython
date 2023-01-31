from funcoes import Funcoes

file_path =  'C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/LabirintWithPython/Anexos/maze/maze3.txt'
f = Funcoes(file_path)
f.print_file()
print(f.txt_to_matriz())
print(f.matrix_to_list(f.txt_to_matriz()))
f.close_file()


