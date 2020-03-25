class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                idx = i
        if idx == len(nums):
            for i in range(len(nums) - 1):
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] < nums[j - 1]:
                        nums[j], nums[j - 1] = nums[j - 1], nums[j]
            return
    
        target = nums[idx + 1]
        tarIdx = idx + 1 
        
        for i in range(idx + 1, len(nums)):
            if nums[idx] < nums[i] <= target :
                target = nums[i]
                tarIdx = i

        nums[idx], nums[tarIdx] = nums[tarIdx], nums[idx]
        for i in range(idx, len(nums)):
            for j in range(len(nums) - 1, i + 1, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        
        return 
        
        