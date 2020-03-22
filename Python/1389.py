class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            num, idx = nums[i], index[i]
            result = result[:idx] + [num] + result[idx:]
        return result
        
        