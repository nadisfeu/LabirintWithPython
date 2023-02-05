from graph import Graph
<<<<<<< HEAD

=======
>>>>>>> feature/grazi

class Funcoes:

    def __init__(self, file_path):
        self.file = open(file_path, 'r')             # Abre o txt
        self.file_content = self.file.read()         # Devolve o conteudo do txt
        self.lines = self.file_content.splitlines()  # Transforma cada linha em um elemento na lista
        self.num_lines = len(self.lines)             # Devolve o numero de linhas
        self.element = self.elements_count()               # Devolve o numero de vertices
        self.graph = Graph(self.element)
<<<<<<< HEAD

=======
        self.start, self.end = None, None


>>>>>>> feature/grazi
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
<<<<<<< HEAD
        
=======
    
>>>>>>> feature/grazi
    def make_graph(self):
        # olhar no de baixo e no do lado direito, linha por linha e fazer as ligações
        # se for 1, se for 0, ignora, olhar pela matriz ou direto no txt
        # ou fz todas as ligações laterais, dps verticais
        node = 0
<<<<<<< HEAD
        matrix = self.txt_to_matriz()
        count1 = self.num_lines - 1
        count2 = len(self.lines[0])

        for i in range(count1):  # pega a quantidade de linhas, menos a ultima
            for j in range(count2):  # pega a quantidade de colunas
                if matrix[i][j] == 1:
                    if j + 1 > count2:
                        pass
                    elif matrix[i][j+1] == 1:
                        self.graph.add_undirected_edge(node, node + 1)  # verifica a direita
                    if matrix[i+1][j] == 1:
                        self.graph.add_undirected_edge(node, node + (len(self.lines[0])))  # verifica embaixo
                node += 1

        # for c in range(len(self.lines[0]) - 1):  # especial pra ultima linha que nao tem embaixo
        #     if matrix[self.num_lines - 1][c] == 1:
        #         if matrix[self.num_lines - 1][c+1] == 1:
        #             self.graph.add_undirected_edge(node, node + 1)  # verifica a direita

    def make_graph2(self):
        node = 0

        for i in range(self.num_lines - 1):  # pega a quantidade de linhas, menos a ultima
            for j in range(len(self.lines[i])):  # pega a quantidade de colunas

                if self.lines[i][j] != '#':
                    if j + 1 < len(self.lines[i]):
                        if self.lines[i][j + 1] != '#':
                            self.graph.add_undirected_edge(node, node + 1)  # verifica a direita
                    if self.lines[i + 1][j] != '#':
                        self.graph.add_undirected_edge(node, node + (len(self.lines[0])))  # verifica embaixo
                node += 1
=======

        for i in range(self.num_lines - 1):  # pega a quantidade de linhas, menos a ultima
            for j in range(len(self.lines[i])):  # pega a quantidade de colunas
                if self.lines[i][j] != '#':
                    if self.lines[i][j] != '#':
                        if self.lines[i][j] == 'S':
                            self.start = node
                        if self.lines[i][j] == 'E':
                            self.end = node
                        self.graph.add_undirected_edge(node, node + 1)  # verifica a direita
                    if self.lines[i + 1][j] != '#':
                        if self.lines[i+1][j] == 'E':
                            self.start = node
                        if self.lines[i+1][j] == 'S':
                            self.end = node
                        self.graph.add_undirected_edge(node, node + (len(self.lines[0])))  # verifica embaixo
                node += 1







                    
>>>>>>> feature/grazi
