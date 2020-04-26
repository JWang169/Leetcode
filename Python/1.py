class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = dict()
        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                return [seen[m], i]
            seen[n] = i
        return [-1, -1]
        
        