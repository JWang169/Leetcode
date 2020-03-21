class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        # dp[i][j] means the longest repeating string ends at i and j. 
        # (aka the target ends at i and the repeating one ends at j)
        n = len(S) + 1
        dp = [[0] * n for _ in range(n)]
        result = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                if S[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                    result = max(result, dp[i][j])        
        
        return result 

    # TLE
    def longestRepeatingSubstring(self, S: str) -> int:
        if not S:
            return 0
        result = 0
        for i in range(len(S) - 1):
            for length in range(1, len(S)):
                target = S[i: i + length]
                for j in range(i + 1, len(S) - length + 1):
                    if S[j: j + length] == target:
                        result = max(result, length)
                                  
        return result 