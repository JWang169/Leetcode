class Solution:
    # undirected: Union Find
    # directed: Topological Sort
    def validTree(self, n: int, edges: List[List[int]]) -> bool:   
        self.graph = {}
        count = 0
        for u, v in edges:
            rootU = self.find(u)
            rootV = self.find(v)
            # circle
            if rootU == rootV:
                return False 
            count += 1 
            self.graph[rootU] = rootV
        return count == n - 1
    
    
    def find(self, u):
        if u not in self.graph:
            self.graph[u] = u
            return u
        paths = []
        while self.graph[u] != u:
            paths.append(u)
            u = self.graph[u]
        for path in paths:
            self.graph[u] = u
        return u