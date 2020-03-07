from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Build the graph:
        self.graph = defaultdict(list)
        for a, b in connections:
            self.graph[a].append(b)
            self.graph[b].append(a) 

        self.res = []
        self.visited = set()
        self.low = {}

        self.dfs(0, -1, 0) # step, prevNode, currentNode 
        return self.res
    
    def dfs(self, depth, prevNode, node):
        """
        @param depth: indicates the depth of the current dfs search
        @param prevNode: last node before current node
        @param node: starting point of this dfs
        """
    
        # recursive - dfs with an implicit stack
        self.visited.add(node)
        self.low[node] = depth

        for n in self.graph[node]:
            if n == prevNode:     
                continue  
            if n not in self.visited:
                self.dfs(depth + 1, node, n) # dfs search its child node, so the depth increases by 1
            self.low[node] = min(self.low[node], self.low[n])  
            if depth < self.low[n]:
                self.res.append([node, n])

