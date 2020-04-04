class Solution:
    def canWin(self, s: str) -> bool:
        self.seen = {}
        return self.dfs(s)
        
    def dfs(self, s):
        if s in self.seen:
            return self.seen[s]
        
        if s.find("++") == -1:
            self.seen[s] = False 
            return False 
        
        for i in range(len(s) - 1):
            if s[i: i + 2] == "++":
                if not self.dfs(s[:i] + "--" + s[i + 2:]):
                    self.seen[s] = True 
                    return True
        self.seen[s] = False 
        return self.seen[s]
        