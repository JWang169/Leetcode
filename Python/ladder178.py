class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        self.graph = {}
        count = 0
        for a, b in edges:
            rootA = self.find(a)
            rootB = self.find(b)
            if rootA == rootB:
                return False 
            count += 1 
            self.graph[rootA] = rootB  
        return count == n - 1
    
    def find(self, a):
        if a not in self.graph:
            self.graph[a] = a 
            return a 
        while a != self.graph[a]:
            a = self.graph[a]
        return a 