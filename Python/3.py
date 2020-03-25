class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 0:
            return s
        
        n = len(s) 
        f = [[False] * n for _ in range(n)]
        maxLength = 1        
        index = 0
        
        for i in range(n):
            f[i][i] = True 
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] = True 
                maxLength = 2
                index = i
        
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if f[i + 1][j - 1] and s[i] == s[j]:
                    f[i][j] = True
                    if j - i + 1 > maxLength:
                        maxLength = j - i + 1
                        index = i
        return s[index: index + maxLength]
                    
                
                