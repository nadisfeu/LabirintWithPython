
class Funcoes:

    def __init__(self, file_name=str):
        self.file = open(file_name, 'r')
        self.file_content = self.file.read()
        self.lines = self.file_content.splitlines()  # Transforma cada linha em um elemento na lista
        self.num_lines = len(self.lines)

    def _node_count(self) -> int:
        count = 0
        for line in self.lines:
            count = count + len(line)
        return count

    def print_file(self):
        print(self.file_content)
