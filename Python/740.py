class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = 10001
        buckets = [0] * n 
        for num in nums:
            buckets[num] += num
        
        dp = [0] * n
        for i in range(1, n):
            
            prev = dp[i - 2] if i > 1 else 0
            dp[i] = max(dp[i - 1], prev + buckets[i])
        # print(dp)
        return dp[-1]
        
        
        