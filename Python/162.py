class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid 
            if nums[mid - 1] > nums[mid]:
                right = mid 
            elif nums[mid + 1] > nums[mid]:
                left = mid
        
        return left if nums[left] > nums[right] else right
