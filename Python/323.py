class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # key: num, val: 
        self.graph = {}
        for i in range(n):
            self.graph[i] = i
        for u, v in edges:
            self.union(u, v) 
        parents = set()
        for i in range(n):
            parent = self.find(i)
            if parent not in parents:
                parents.add(parent)
            
        return len(parents)
            
    def find(self, u):
        paths = []
        while self.graph[u] != u:
            paths.append(u)
            u = self.graph[u]
        for p in paths:
            self.graph[p] = u
        return u
        
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        self.graph[rootU] = self.graph[rootV]
        
        