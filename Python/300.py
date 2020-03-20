# mar 19
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        f = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[j] + 1, f[i])
        return max(f)
                

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f = [1] * len(nums)
        result = 1
        for i in range(0, len(nums)):
            f[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[j] + 1, f[i])
            result = max(result, f[i])
        return result 