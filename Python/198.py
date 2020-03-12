class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]
        for i in range(len(nums)):
            if i == 0:
                dp.append(nums[i])
                continue 
            cur = max(dp[i - 1] + nums[i], dp[i])
            dp.append(cur)
        return dp[-1]