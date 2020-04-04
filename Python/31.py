# April 3rd
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1 
            
        if i == 0:
            nums.reverse()
            return 
        # k is the turning point. nums increase from last num to i, but drop at k
        k = i - 1
        j = len(nums) - 1
        # find the first(smallest) num greater than nums[k] on its right
        while nums[j] <= nums[k]:
            j -= 1 
        nums[k], nums[j] = nums[j], nums[k]
        # reverse the second part
        left, right = k + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -= 1 
            
    

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
        
        