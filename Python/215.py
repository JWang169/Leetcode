class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k > len(nums):
            return -1
        self.partition(nums, 0, len(nums) - 1, k)
        return nums[k - 1]
    
    def partition(self, nums, start, end, k):
        if start == end:
            return 
            
        left, right = start, end 
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1 
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        

        if start <= k - 1 <= right:
            self.partition(nums, start, right, k)
        else:
            self.partition(nums, left, end, k)
            
        