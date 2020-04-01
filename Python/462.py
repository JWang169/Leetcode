class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # find median?
        n = len(nums)
        idx = n // 2
        nums.sort()
        median = nums[idx]
        m1 = 0
        for num in nums:
            m1 += abs(median - num)
        
        return m1
        
        
        