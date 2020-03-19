class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        f = [[False] * n for _ in range(m)]
        
        # initialize
        f[0][0] = True
        
        # this step starts from one 
        for j in range(1, n):
            if p[j - 1] == "*":
                f[0][j] = f[0][j - 1] 
        
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    # match non, match one, or match many
                    f[i][j] = f[i][j - 1] or f[i - 1][j - 1] or f[i - 1][j]
                    continue
                
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    f[i][j] = f[i - 1][j - 1]
                    
        return f[-1][-1]