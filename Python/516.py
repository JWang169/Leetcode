class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        n = len(s)
        
        result = 1
        f = [[1] * n for _ in range(n)]           
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2
                result = 2
        
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                f[i][j] = max(f[i][j - 1], f[i + 1][j])
                if s[i] == s[j]:
                    f[i][j] = max(f[i + 1][j - 1] + 2, f[i][j])
                
                result = max(result, f[i][j])
        return result 