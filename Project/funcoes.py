from graph import Graph

class Funcoes:

    def __init__(self, file_path):
        self.file = open(file_path, 'r')             # Abre o txt
        self.file_content = self.file.read()         # Devolve o conteudo do txt
        self.lines = self.file_content.splitlines()  # Transforma cada linha em um elemento na lista
        self.num_lines = len(self.lines)             # Devolve o numero de linhas
        self.element = self.elements_count()               # Devolve o numero de vertices
        self.graph = Graph(self.element)
        self.start, self.end = None, None


    def elements_count(self) -> int:
        count = 0
        for line in self.lines:
            count = count + len(line)
        return count

    def print_file(self):
        print(self.file_content)

    def close_file(self):
        self.file.close()

    def txt_to_matriz(self): 
        matrix = []
        for line in self.lines:
            row = [1 if c == ' ' else 2 if c in ['S'] else 3 if c in ['E'] else 0 for c in line.strip()]
            matrix.append(row)
        return matrix


    def make_graph(self):
        # olhar no de baixo e no do lado direito, linha por linha e fazer as ligações
        # se for 1, se for 0, ignora, olhar pela matriz ou direto no txt
        # ou fz todas as ligações laterais, dps verticais
        node = 0

        for i in range(self.num_lines - 1):  # pega a quantidade de linhas, menos a ultima
            for j in range(len(self.lines[i])):  # pega a quantidade de colunas
                if self.lines[i][j] != '#':
                    if self.lines[i][j] == 'S':
                        self.start = node
                    if self.lines[i][j] == 'E':
                        self.end = node
                    if j+1<len(self.lines[i]):
                        if self.lines[i][j+1] != '#':
                            self.graph.add_undirected_edge(node, node + 1)  # verifica a direita
                    if self.lines[i + 1][j] != '#':
                        self.graph.add_undirected_edge(node, node + (len(self.lines[0])))  # verifica embaixo
                node += 1


def busca(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    # Marca o vértice atual como visitado
    visited.add(start)
    # Verifica se o vértice atual é o destino
    if start == end:
        return [start]
    # Para cada vizinho do vértice atual
    for neighbor in graph.get_neighbors(start):
        # Se o vizinho ainda não foi visitado
        if neighbor not in visited:
            # Realiza a busca em profundidade a partir do vizinho
            path = busca(graph, neighbor, end, visited)
            # Se a busca retornou um caminho válido, adiciona o vértice atual ao caminho
            if path is not None:
                return [start] + path
    # Se não há um caminho válido a partir do vértice atual, retorna None
    return None







