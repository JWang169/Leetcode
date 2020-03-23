class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # dfs 
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        self.result = 0
        self.dfs(edges[0][0], None, graph)
        return self.result
     
    # def bfs(self, node, graph):
        
    def dfs(self, node, prev, graph):
        # longest path through a node is sum of top 2 depths of children's tree
        firstDepth, secondDepth = 0, 0
        for child in graph[node]:
            # only one way 
            if child == prev:
                continue 
            childDepth = self.dfs(child, node, graph)
            if childDepth > firstDepth:
                firstDepth, secondDepth = childDepth, firstDepth
            elif childDepth > secondDepth:
                secondDepth = childDepth

        self.result = max(self.result, firstDepth + secondDepth)
        return firstDepth + 1
        
        
        
#     dfs solution TLE
#     def search(self, node, prev, count, graph):
#         self.result = max(self.result, count)
#         if node not in graph:
#             return 
#         children = graph[node]
#         for child in children:
#             if child == prev:
#                 continue
#             self.search(child, node, count + 1, graph)
#         return 
    
        