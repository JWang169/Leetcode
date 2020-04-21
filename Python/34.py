class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else[-1, -1]
        
        left, right = 0, len(nums) - 1
        idx = -1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                idx = mid
                break
            if nums[mid] > target:
                right = mid 
            else:
                left = mid 
        
        if idx == -1:
            if nums[left] == target:
                idx = left
            elif nums[right] == target:
                idx = right 

        if idx == -1:
            return [-1, -1]
        
        # find left border
        left, right = 0, idx
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                right = mid 
            else:
                left = mid
        
        if nums[left] == target:
            start = left
        else:
            start = right
        # find right border       
        left, right = idx, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                left = mid 
            else:
                right = mid - 1
        if nums[right] == target:
            end = right
        else:
            end = left
        return [start, end]     
        
        
        