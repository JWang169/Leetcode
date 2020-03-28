class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 1. There is a loop in the graph, and no vertex has more than 1 parent
        # 2. a vertex has more than 1 parent, but no loop in  the graph
        # 3. a vertex has more than 1 parent, and it is part of a loop
        
        
        candidates = []
        parents = dict()
        self.graph = dict()
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append([parents[v], v])
                candidates.append([u, v])
        
        if candidates:
            # one vertex has two parents
            return candidates[0] if self.hasCircle(candidates[0], parents) else candidates[1]
        
        # There is a loop in the graph and no vertex has more than 1 parent
        # find the loop

        for u, v in edges:
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u == root_v:
                return [u, v]
            self.graph[root_v] = root_u
        
        return None
    
    
    def hasCircle(self, edge, parents):
        u, v = edge
        while u != v and u in parents:
            u = parents[u]
        return u == v
        
    
    
    def find(self, u):
        if u not in self.graph:
            self.graph[u] = u
            return u
        while u != self.graph[u]:
            u = self.graph[u]
        return u
            