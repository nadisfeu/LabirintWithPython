maze = open(r'Anexos\maze\maze3.txt', 'r')
content = maze.read()
lines = content.splitlines()  # Transforma cada linha em um elemento na lista
num_lines = len(lines)  # Separa a quantidade de linhas
print(num_lines)

matriz_adj = []

for u in range(num_lines): #
    print("lines:", u,  lines[u])
    matriz_adj.append([])  # Adiciona mais uma linha na matriz
    for i in lines[u]:     # Diz onde vai ser 0 e onde vai ser 1
        if i == ' ' or i == 'S' or i == 'E':
            matriz_adj[u].append(0)
        else:
            matriz_adj[u].append(1)

for i in matriz_adj:
    print(i)

    # Corrigir o tamamnho de todas as linhas
