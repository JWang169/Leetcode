class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # A = [4,7,9,10], K = 3
        # left:  0   2   
        # right: 3   3
        # mid:   1   2
        # start: 4   7
        # end :  7   9
        # 1. 7 - 4     1 - 0 + 3
        left, right = 0, len(nums) - 1
        
        missingNums = nums[right] - nums[left] + 1 - len(nums)
        if missingNums < k:
            return nums[right] + k - missingNums
        
        while left + 1 < right:
            mid = (left + right) // 2
            start, end = nums[left], nums[mid]
            missing = end - start - (mid - left)
            if missing >= k:
                right = mid
            else:
                left = mid
                k -= missing
        
        
        return nums[left] + k