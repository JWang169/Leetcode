class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1 
        
        left, right = 0, len(nums) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            
            
            if nums[mid] > nums[left]:
                if nums[left] < target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target < nums[right]: 
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1 
                