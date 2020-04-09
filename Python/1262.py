class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][j]: the maximum sum of nums[:i] which modulos 3 equals to j
        dp = [[0] * n for _ in range(3)]
        start = nums[0] % 3
        dp[start][0] = nums[0]
        
        for i in range(1, n):
            for j in range(3):
                prev = dp[(j - nums[i]) % 3][i - 1]
                cur = prev + nums[i]
                if cur % 3 == j:
                    dp[j][i] = max(dp[j][i - 1], cur)
                else:
                    dp[j][i] = dp[j][i - 1]
                
                
        return dp[0][n - 1]