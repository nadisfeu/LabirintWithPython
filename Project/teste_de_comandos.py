# for u in range(num_lines):
#     print("lines:", u,  lines[u])
#     matriz_adj.append([])  # Adiciona mais uma linha na matriz
#     for i in lines[u]:     # Diz onde vai ser 0 e onde vai ser 1
#         if i == ' ':
#             matriz_adj[u].append(1)
#         elif i == 'S':
#             matriz_adj[u].append(2)
#         elif i == 'E':
#             matriz_adj[u].append(3)
#         else:
#             matriz_adj[u].append(0)

from funcoes import Funcoes

f = Funcoes(r'Anexos/maze/maze3.txt')
f.print_file()
