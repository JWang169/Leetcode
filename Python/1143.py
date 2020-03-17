class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 转移方程是f[i][j] = max(f[i-1][j], f[i][j -1], f[i-1][j-1] + 1|a[i-1] == b[i-1])
        m, n = len(text1) + 1, len(text2) + 1  # 前m，n个 
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                dp[i][j] = max(dp[i- 1][j], dp[i][j - 1])
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]
        
        
        