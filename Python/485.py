class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            result = max(result, count)
        return result