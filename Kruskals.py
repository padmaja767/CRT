class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []
    
    def addEdge(self, start, end, wt):
        self.graph.append([start, end, wt])
    
    def find(self, parent, z):
        if parent[z] != z:
            parent[z] = self.find(parent, parent[z])
        return parent[z]
    
    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])
        result = []
        parent = list(range(self.V))
        rank = [0] * self.V
        node = 0
        
        while len(result) < self.V - 1:
            u, v, wt = self.graph[node]
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                result.append([u, v, wt])
                self.union(parent, rank, x, y)
            
            node += 1
        
        cost = 0
        for p, q, r in result:
            cost += r
        
        print("Minimum Spanning Tree:")
        print(result)
        return cost
    
    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

# Example usage:
gg = Graph(7)
gg.addEdge(0, 1, 7)
gg.addEdge(0, 3, 5)
gg.addEdge(1, 2, 8)
gg.addEdge(1, 3, 9)
gg.addEdge(1, 4, 7)
gg.addEdge(2, 4, 5)
gg.addEdge(3, 4, 15)
gg.addEdge(3, 5, 6)
gg.addEdge(4, 5, 8)
gg.addEdge(4, 6, 9)
gg.addEdge(5, 6, 11)

print(gg.kruskal())
