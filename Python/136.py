#  XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


# 复习了一遍quickSort
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None 
        self.quickSort(nums, 0, len(nums) - 1)
        i, n = 0, len(nums)
        while i < n:
            if i + 1 < n and nums[i + 1] != nums[i]:
                if i > 0 and nums[i - 1] == nums[i]:
                    return nums[i + 1]
                else:
                    return nums[i]
            i += 2
        return nums[-1]
        
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return 
        left, right = start, end
        pivot = nums[(left + right) // 2 ]
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
        
        