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
        matrix = self.txt_to_matriz()

        for i in range(self.num_lines - 1):  # pega a quantidade de linhas, menos a ultima
            for j in range(len(self.lines[0])):  # pega a quantidade de colunas
                if matrix[i][j] != 0:
                    if matrix[i][j] != 0:
                        if matrix[i][j] == 2:
                            self.start = node
                        if matrix[i][j] == 3:
                            self.end = node
                        self.graph.add_undirected_edge(node, node + 1)  # verifica a direita
                    if matrix[i+1][j] != 0:
                        if matrix[i + 1][j] == 2:
                            self.start = node
                        if matrix[i + 1][j]== 3:
                            self.end = node
                        self.graph.add_undirected_edge(node, node + (len(self.lines[0])))  # verifica embaixo
                node += 1








                    