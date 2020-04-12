class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # 0: not visited, 1: safe, 2: unsafe
        history = [0] * len(graph)
        result = []
        for i in range(len(graph)):
            if self.dfs(graph, i, history):
                result.append(i)
        return sorted(result)

    
    def dfs(self, graph, i, history):
        if history[i] != 0:
            return history[i] == 1
        history[i] = 2
        for node in graph[i]:
            if not self.dfs(graph, node, history):
                return False 
        history[i] = 1
        return True 
        
        