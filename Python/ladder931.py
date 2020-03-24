class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        if not nums:
            return 0.0
            
        size = sum(len(arr) for arr in nums)
        if size == 0:
            return 0.0
            
        if size % 2 == 0:
            return (self.findKth(nums, size // 2 + 1) + self.findKth(nums, size // 2)) / 2
        else:
            return self.findKth(nums, size // 2 + 1)
    
    
    def findKth(self, nums, k):
        start, end = self.getRange(nums)
        while start + 1 < end:
            mid = (start + end) // 2 
            if self.countNums(nums, mid) >= k:
                end = mid 
            else:
                start = mid 
        if self.countNums(nums, start) >= k:
            return start
        return end 

    def countNums(self, nums, target):
        count = 0
        for arr in nums:
            count += self.helper(arr, target)
        return count 
        
        
    def helper(self, arr, val):
        if not arr:
            return 0
        left, right = 0, len(arr) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            if arr[mid] > val:
                right = mid 
            else:
                left = mid
                
        if arr[left] > val:
            return left 
        elif arr[right] > val:
            return right 
        return right + 1 
        
        
    
    def getRange(self, nums):
        mi, ma = sys.maxsize, -sys.maxsize 
        for array in nums:
            if not array:
                continue
            mi = min(mi, array[0])
            ma = max(ma, array[-1])
        return mi, ma 
            