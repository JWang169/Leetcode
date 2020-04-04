# Apr 4
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        while p0 < len(nums) and p1 < len(nums):
            while p0 < len(nums) and nums[p0] != 0:
                p0 += 1 
            while p1 < len(nums) and nums[p1] == 0:
                p1 += 1 
            if p1 < len(nums) and p0 < p1:
                nums[p1], nums[p0] = nums[p0], nums[p1]
            else:
                p1 += 1 
        


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0  # left to mark zero
        while right < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1 
            right = left 
            while right < len(nums) and nums[right] == 0:
                right += 1 
            if left < len(nums) and right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right += 1 