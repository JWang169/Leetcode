class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        if n == 1:
            return []
        self.result = []
        self.dfs(n, [])
        return self.result
    
    
    def dfs(self, n, factors):
        if n <= 1 and len(factors) > 1:
            self.result.append(factors)
            return 
        
        if not factors:
            start = 2
        else:
            start = factors[-1]
        
        for i in range(start, n + 1):
            if i > n / i:
                break
            if n % i == 0:
                self.dfs(n // i, factors + [i])
                
        if n >= start:      
            self.dfs(1, factors + [n])
        