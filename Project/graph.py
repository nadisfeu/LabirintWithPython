class Graph:
    def __init__(self, node_count: int, edge_count: int = 0, adj_list: list[list[int]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        self.is_connected = False
        if adj_list == []:
            for i in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append(v)
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def degree_out(self, u: int) -> int:
        return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:
        degree = 0
        for i in range(len(self.adj_list)):
            if u in self.adj_list[i]:
                degree += 1
        return degree

    def highest_degree_out(self) -> int:
        max_degree_out = 0
        highest_degree_node = 0
        for u in range(self.node_count):
            degree_out_node_u = self.degree_out(u)
            if max_degree_out < degree_out_node_u:
                max_degree_out = degree_out_node_u
                highest_degree_node = u
        return highest_degree_node

    def highest_degree_in(self) -> int:
        max_degree_in = float("inf")
        highest_degree_node = 0
        for u in range(self.node_count):
            degree_in_node_u = self.degree_in(u)
            if max_degree_in < degree_in_node_u:
                max_degree_in = degree_in_node_u
                highest_degree_node = u
        return highest_degree_node

    def density(self):
        return self.edge_count / (self.node_count * (self.node_count - 1))

    def complete(self):
        return self.density() == 1

    def regular(self):
        degree = len(self.adj_list[0])
        for u in range(1, len(self.adj_list)):
            if len(self.adj_list[u]) != degree:
                return False
        return True

    def complement(self):
        g2 = Graph(self.node_count, adj_list=[])
        for u in range(len(self.adj_list)):
            for v in range(self.node_count):
                if v not in self.adj_list[u] and v != u:
                    g2.add_undirected_edge(u, v)
        return g2

    def subgraph(self, g2):
        if g2.node_count > self.node_count or g2.edge_count > self.edge_count:
            return False
        for u in range(len(g2.adj_list)):
            for v in g2.adj_list[u]:
                if v not in self.adj_list[u]:
                    return False
        return True


    def bfs(self, s):
        desc = [0 for v in range(self.node_count)]
        Q = [s]
        R = [s]
        desc[s] = 1
        while Q:
            u = Q.pop(0)
            for v in self.adj_list[u]:
                if desc[v] == 0:
                    Q.append(v)
                    R.append(v)
                    desc[v] = 1

        if len(R) == self.node_count:
            self.is_connected = True

        return R

    def connected(self):
        return self.is_connected
        
    def is_neighbor(self, u, v):
        return v in self.adj_list[u]

    def to_adj_matrix(self):
        adj_matrix = [[0 for _ in range(self.node_count)] for j in range(self.node_count)]
        for i in range(self.node_count):
            for j in self.adj_list[i]:
                adj_matrix[i][j] = 1
        return adj_matrix

    def is_valid_walk(self, walk: list[int]): #passeio aberto
        for i in range(len(walk) - 1):
            if walk[i + 1] not in self.adj_list[walk[i]]:
                return False
        return True
    

    def is_closed(self, walk: list[int]): #passeio fechado
        return walk[0] == walk[-1] 


    def is_valid_path(self, path: list[int]): #caminho - nao repete vertice, nem aresta
        if len(path) <= 1:
            return False
        for i in range(len(path) - 1):
            if path[i + 1] not in self.adj_list[path[i]] or path.count(path[i]) > 1 or path.count(path[i + 1]) > 1:
                return False
        return True

    def __str__(self):
        repr = ""
        for adj in self.adj_list:
            repr += str(adj) + "\n"
        return repr