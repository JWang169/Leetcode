class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            ch = int(s[i - 1])
            if ch == 0:
                if i == 1:
                    return 0
                if int(s[i - 2]) > 2 or int(s[i - 2]) == 0:
                    return 0
                dp[i] = dp[i - 2]
                continue 
            if i == 1:
                dp[i] = 1
                continue
                
            dp[i] += dp[i - 1]
            
            if i > 1 and s[i - 2] == '1':
                dp[i] += dp[i - 2]
            if i > 1 and s[i - 2] == '2' and ch <= 6:
                dp[i] += dp[i - 2]
                
        return dp[-1]
                