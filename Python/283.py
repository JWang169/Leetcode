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