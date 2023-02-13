from funcoes import *
import time


arquivo = 1
while arquivo!=0:
    start = time.time()
    arquivo = input("Informe o arquivo (0 para sair):\nExemplo: " + "maze3\n").lower().replace(" ", "")
    file_path = 'Anexo/maze/' + arquivo + '.txt'
    f = Funcoes(file_path)
    print("Labirinto\n")
    f.print_file()
    print("--------------------------------------")
    f.make_graph()
    #print(f.graph)
    #print("--------------------------------------")
    print("Entrada labirinto:", f.start)
    print("Saida labirinto:", f.end)
    print(f.print_coordinates_path())
    print(busca(f.graph, f.start, f.end))
    end = time.time()
    tempo_de_execucao = end - start
    print("Tempo de execução:", tempo_de_execucao, "segundos\n")

