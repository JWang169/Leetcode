class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 1:
            return []
        self.results = list()
        self.dfs([], n, 2, n - 1)
        return self.results
    
    
    def dfs(self, cur, n, first, last):
        if n == 1:
            self.results.append(cur)
            return 
        for i in range(first, last + 1):
            if n % i == 0:
                self.dfs(cur + [i], n // i, i, n // i)
                
        
        
        