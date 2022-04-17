# Kosaraju's algorithm to find strongly connected components in Python
import random

from collections import defaultdict

count = 0 
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    def __repr__(self):
        return str(self.V), str(self.graph)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        global count
        visited_vertex[d] = True
        print(d, end=',')
        print(f"{self.graph}@")

        count += 1

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
        print(self.graph)
        visited_vertex = [False] * (self.V)

        print(self.V)
        for i in range(self.V):
            print(i)
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()
        print(gr.graph)
        print(self.graph)

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")


g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)
# for i in range(0, 25):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(25, 50):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(50, 75):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(75, 100):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))        

# for i in range(100, 125):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(125, 150):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(150, 175):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(175, 200):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500)) 

# for i in range(200, 225):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(225, 250):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(250, 275):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(275, 300):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500)) 

# for i in range(300, 325):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(325, 350):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(350, 375):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(375, 400):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(0, 500)) 

# for i in range(400, 425):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(425, 450):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(450, 475):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500))

# for i in range(475, 500):
#     for j in range(random.randint(0, 25)):
#         g.add_edge(i, random.randint(random.randint(0, 500), 500)) 


    
print("Strongly Connected Components:")
g.print_scc()
print(f"The count is: {count}")
