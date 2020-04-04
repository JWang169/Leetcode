class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        letters = collections.Counter(s)
        mid = []
        for ch, num in letters.items():
            if num % 2 == 1:
                mid.append(ch)
        if len(mid) > 1:
            return []
        mid = mid[0] if mid else ""
        self.res = []
        n = len(s) // 2
        self.dfs(n, "", letters, mid)
        return self.res 
    
    
    def dfs(self, n, cur, letters, mid):
        if len(cur) == n:
            self.res.append(cur + mid + cur[::-1])
            return 
        for ch, num in letters.items():
            if num > 1:
                letters[ch] -= 2
                self.dfs(n, cur + ch, letters, mid)
                letters[ch] += 2
        
                
        
        
        
        
        
        