from funcoes import Funcoes


def busca(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    # Marca o vértice atual como visitado
    visited.add(start)
    # Verifica se o vértice atual é o destino
    if start == end:
        return [start]
    # Para cada vizinho do vértice atual
    for neighbor in f.graph.get_neighbors(start):
        # Se o vizinho ainda não foi visitado
        if neighbor not in visited:
            # Realiza a busca em profundidade a partir do vizinho
            path = busca(graph, neighbor, end, visited)
            # Se a busca retornou um caminho válido, adiciona o vértice atual ao caminho
            if path is not None:
                return [start] + path
    # Se não há um caminho válido a partir do vértice atual, retorna None
    return None


file_path =  'C:/Users/grazi/OneDrive/Área de Trabalho/Arquivos/LabirintWithPython/Anexo/maze/maze3.txt'
f = Funcoes(file_path)
f.print_file()
for i in f.txt_to_matriz():
    print(i)
print("**********************")
f.make_graph()
print(f.graph)
print("**********************")
print(f.start)
print(f.end)
print(busca(f.graph, f.start, f.end))
f.close_file()


