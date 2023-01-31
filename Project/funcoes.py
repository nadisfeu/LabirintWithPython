
class Funcoes:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')             # Abre o txt
        self.file_content = self.file.read()         # Devolve o conteudo do txt
        self.lines = self.file_content.splitlines()  # Transforma cada linha em um elemento na lista
        self.num_lines = len(self.lines)             # Devolve o numero de linhas
        self.node = self.node_count()               # Devolve o numero de vertices

    def node_count(self) -> int:
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
            row = [1 if c in [' ', '/0'] else 2 if c in ['S', 'E'] else 0 for c in line]
            matrix.append(row)

        for i in range(len(matrix)):
            while len(matrix[i]) != len(matrix[0]):
                matrix[i].append(1) 
        return matrix
        
    def adjacency_matrix_to_list(self, adj_matrix):
        adj_list = []
        for i in range(len(adj_matrix)):
            vertex = [j for j, x in enumerate(adj_matrix[i]) if x == 1 or x == 2]
            if 2 in adj_matrix[i]:
                vertex.insert(0, "entry")
                vertex.append("exit")
            adj_list.append(vertex)
        return adj_list













