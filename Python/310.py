class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        graph = dict()
        for i in range(n):
            graph[i] = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        while n > 2:
            newLeaves = []
            n -= len(leaves)
            for leaf in leaves:
                parents = graph[leaf]
                for parent in parents:
                    graph[parent].remove(leaf)
                    if len(graph[parent]) == 1:
                        newLeaves.append(parent)
                leaves = newLeaves
        return leaves