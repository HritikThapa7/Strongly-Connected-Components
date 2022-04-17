from collections import defaultdict
import sys

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):        
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end=',')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = defaultdict(bool)
        for i in list(self.graph.keys()):
            visited_vertex[i] = False

        for i in list(visited_vertex.keys()):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        for node in visited_vertex.keys():
            visited_vertex[node] = False
        

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")

if __name__ == "__main__":
    val = str(sys.argv[1])
    with open(val, "r") as f:
        lines = f.readlines()
        v = len({c.strip() for line in lines for c in line.split()[:2]})
        g = Graph(v)
        for line in lines:
            a, b = [c.strip() for c in line.split()][:2]
            g.add_edge(int(a), int(b))
    g.print_scc()
    
