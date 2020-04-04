class Solution:
    def fib(self, N: int) -> int:
        self.seen = {}
        self.seen[0] = 0
        self.seen[1] = 1
        return self.dfs(N)
    
    
    def dfs(self, n):
        if n in self.seen:
            return self.seen[n]
        self.seen[n] = self.dfs(n - 1) + self.dfs(n - 2)
        return self.seen[n]
        
        