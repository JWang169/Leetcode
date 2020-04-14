class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        self.results = set()
        for i in range(10):
            self.dfs(i, low, high)
        res = sorted(list(self.results))
        return res
    
    
    def dfs(self, cur, low, high):
        if cur > high:
            return 
        if low <= cur <= high:
            self.results.add(cur)
   
        last = cur % 10
        if last + 1 <= 9:
            self.dfs(cur * 10 + last + 1, low, high)
        if last - 1 >= 0:
            self.dfs(cur * 10 + last - 1, low, high)
        
        
        