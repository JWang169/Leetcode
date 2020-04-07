class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # dp[i][j]: how many choices we have with i dices and the last face is j
        # again dp[i][j] means the number of distinct sequences that can be obtained when rolling i times and ending with j
        MOD = 10 ** 9 + 7
        dp = [[0] * 7 for i in range(n + 1)]
        
        # dp[1][i]: roll once, end with i => only one possible sequence. so dp[1][i] = 1
        for i in range(6):
            dp[1][i] = 1
        
        # total 
        dp[1][6] = 6
                
        for i in range(2, n + 1):
            total = 0
            for j in range(6):
                # if there is no constrains, the total sequences ending with j should be the total sequences from previous rolling
                dp[i][j] = dp[i - 1][6]
                # for axx1, only 111 is not allowed, so we need to remove 1 sequence from previous sum
                if i - rollMax[j] == 1:
                    dp[i][j] -= 1
                # for axx1, we need to remove the number of a11(211, 311, 411...)
                if i - rollMax[j] >= 2:
                    reduction = dp[i - rollMax[j] - 1][6] - dp[i - rollMax[j] - 1][j]
                    dp[i][j] = ((dp[i][j] - reduction) % MOD + MOD) % MOD
                total = (total + dp[i][j]) % MOD
            dp[i][6] = total
        return dp[n][6]
        
        
        
        