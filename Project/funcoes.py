
class Funcoes:

    def __init__(self, file_name=str):
        self.file = open(file_name, 'r')             # Abre o txt
        self.file_content = self.file.read()         # Devolve o conteudo do txt
        self.lines = self.file_content.splitlines()  # Transforma cada linha em um elemento na lista
        self.num_lines = len(self.lines)             # Devolve o numero de linhas
        self.node = self._node_count()               # Devolve o numero de vertices

    def _node_count(self) -> int:
        count = 0
        for line in self.lines:
            count = count + len(line)
        return count

    def print_file(self):
        print(self.file_content)

    def _close_file(self):
        self.file.close()
