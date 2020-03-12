class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mi = []
        ma = []
        for i in range(len(nums)):
            if i == 0:
                mi.append(nums[i])
                ma.append(nums[i])
                result = nums[i]
                continue
            ma.append(max(nums[i], nums[i] * ma[-1], nums[i] * mi[-1]))
            mi.append(min(nums[i], nums[i] * ma[-2], nums[i] * mi[-1]))
            result = max(result, ma[-1], mi[-1])
        return result
    
    
    