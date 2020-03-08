class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # 区间型动态规划
        if not values:
            return False 
        n = len(values)
        dp = [[0] * n for _ in range(n)]  # dp[i][j] 表示当前剩余硬币区间为[i, j]时，能够获得的最大值
        
        # 初始化， 1.i == j 2. i + 1 == j
        for i in range(n):
            dp[i][i] = values[i]
        for i in range(n - 1):
            dp[i][i + 1] = max(values[i], values[i + 1])

        total = sum(values)
        # 转换方程 i: bottom-up; j: left-to-right
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j or i + 1 == j:
                    continue
                dp[i][j] = max(values[i] + min(dp[i + 2][j], dp[i + 1][j - 1]), values[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
            
        
        return dp[0][n - 1] > total / 2
            