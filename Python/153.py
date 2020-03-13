class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        left, right = 0, len(nums) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] >= nums[0]:
                if nums[mid] > nums[len(nums) - 1]:
                    left = mid
                else:
                    right = mid
            if nums[mid] < nums[0]:
                right = mid 
                
        return min(nums[left],nums[right])
        
        