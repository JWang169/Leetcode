class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        mappings = {}
        for i, nodes in enumerate(graph):
            mappings[i] = nodes
        
        result = []
        queue = deque([[0]])
        while queue:
            path = queue.popleft()
            last = path[-1]
            if last == N:
                result.append(path)
                continue 
            nexts = mappings[last]
            for nxt in nexts:
                queue.append(path + [nxt])
        return result 
            
        
        