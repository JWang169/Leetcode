class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:return None
        result = -sys.maxsize 
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[0] = nums[i]
            else:
                if dp[i - 1] > 0:
                    dp[i] = dp[i - 1] + nums[i]
                else:
                    dp[i] = nums[i]
            result = max(dp[i], result)
        return result  