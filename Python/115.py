class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] 代表t[:j] 在 s[:i] 中出现的次数
        # 如果b至少在a里出现一次，那么a和b的最长公共子序列就是b，而且不能更长
        # b的最后一个字符一定和a中的某个字符进行了匹配
        # dp[i][j]分两种情况:
        #   1. s[i - 1] == t[j - 1]: dp[i][j] = dp[i - 1][j - 1]
        #   2. s[i - 1] != t[j - 1]: dp[i][j] = dp[i - 1][j]   不需要知道t[j - 1]和s[: i - 1]里面的第几个相等，只需要知道和s[i - 1]不相等
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
                else:
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    dp[i][j] += dp[i - 1][j] 
        return dp[-1][-1]
                
        
        
        