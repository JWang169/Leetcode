class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # quick select
        self.quickSelect(nums, 0, len(nums) - 1, k)
        result = nums[:k]
        result.sort(reverse=True) 
        return result
    
    def quickSelect(self, nums, start, end, k):
        if start >= end:
            return 
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            # 因为要选k largest，就排降序，比pivot大的在左边，小的在右边
            # find element < pivot
            while left <= right and nums[left] > pivot:
                left += 1 
            while left <= right and nums[right] < pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
        
        if start + k - 1 <= right:
            self.quickSelect(nums, start, right, k)
            return 
        if start + k - 1 >= left:
            self.quickSelect(nums, left, end, k - (left - start))
            return 
        return
        
        
        