class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return 
        step = k % len(nums)
        self.swap(nums, 0, len(nums) - step - 1)
        self.swap(nums, len(nums)-step, len(nums) - 1)
        self.swap(nums, 0, len(nums) - 1)
    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -= 1 
        return 