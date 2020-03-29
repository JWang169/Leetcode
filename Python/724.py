class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1 
        
        n = len(nums)
        prefix = [0] * n
        for i in range(n):
            if i == 0:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i - 1] + nums[i]
        
        total = prefix[-1]
        for i in range(n):
            if (prefix[i] - nums[i]) * 2 == total - nums[i]:
                return i
        return -1
        
        