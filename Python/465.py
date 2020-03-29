class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        graph = dict()
        # x gives y money
        for x, y, money in transactions:
            graph[x] = graph.get(x, 0) + money
            graph[y] = graph.get(y, 0) - money 
        
        remains = []
        for val in graph.values():
            if val != 0:
                remains.append(val)
                
        return self.dfs(remains)
        
    
    def dfs(self, remains):
        if not remains:
            return 0
        
        # greedy
        for i in range(1, len(remains)):
            if remains[i] == -remains[0]:
                return 1 + self.dfs(remains[1: i] + remains[i + 1: ])
        
        # non greedy
        minTrans = len(remains)
        for i in range(1, len(remains)):
            if remains[i] * remains[0] < 0:
                remains[i] += remains[0]
                minTrans = min(minTrans, 1 + self.dfs(list(remains[1:])))
                remains[i] -= remains[0]
        return minTrans
                
        
        
    
    
    
    
    
    
    
    