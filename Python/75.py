class Solution:
    def sortColors(self, nums: List[int]) -> None:
        self.quickSort(nums, 0, len(nums) - 1)
        
    def quickSort(self, nums, start, end):
        if start >= end:
            return 
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)
        return 