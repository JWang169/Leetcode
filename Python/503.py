class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        double = nums + nums
        result = []
        n = len(nums)
        for i, num in enumerate(nums):
            found = False
            for j in range(i + 1, i + 1 + n):
                if double[j] > nums[i]:
                    result.append(double[j])
                    found = True
                    break
            if not found:
                result.append(-1)
        return result
        
        
        