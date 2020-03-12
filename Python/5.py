class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        ma = 1
        result = s[0]
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True 
            if i > 0 and s[i - 1] == s[i]:
                dp[i - 1][i] = True 
                result = s[i - 1: i+1]
                ma = 2

        for length in range(3, n + 1):
            # last start idx i = n - length
            for i in range(n - length + 1):
                # end idx j = i + length - 1 
                j = i + length - 1 
                if dp[i + 1][j - 1] == True and s[i] == s[j]:
                    dp[i][j] = True
                    if length > ma:
                        result = s[i : j + 1]
                        ma = length 
        return result