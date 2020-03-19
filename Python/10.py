class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1 
        f = [[False] * n for _ in range(m)]
        
        f[0][0] = True
        
        for j in range(1, n):
            if p[j - 1] == '*' and j >= 2 and f[0][j - 2]:
                f[0][j] = f[0][j - 2]       
        
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*' and j >= 2:
                    # 如果前一个char不match，就只能把前一个用*抹掉，
                    # 所以f[i][j]取决于倒数第二个，就是p[j - 2]
                    if p[j - 2] != '.' and p[j - 2] != s[i - 1]:
                        f[i][j] = f[i][j - 2]
                    else:
                       # 这是'*'前一个char，也就是p[j - 2] match s[i - 1]的情况
                       # 三种情况：match non    or    1            or many 
                        f[i][j] = f[i][j - 2] or f[i - 1][j - 2] or f[i - 1][j]
                        
                elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    f[i][j] = f[i - 1][j - 1] 
                    
        return f[-1][-1]
        