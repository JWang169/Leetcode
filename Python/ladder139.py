import sys 
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        mappings = {}
        preSum = 0
        mappings[0] = -1
        for i, num in enumerate(nums):
            cur = num + preSum
            preSum = cur
            if cur in mappings:
                return mappings[cur] + 1, i 
            mappings[cur] = i
        
        sums = list(mappings.keys())
        sums.sort()

        closest = sys.maxsize 
        result = [-1, 0]
        for i in range(len(sums)):
            if abs(sums[i] - sums[i - 1]) < closest:
                result = [mappings[sums[i - 1]], mappings[sums[i]]]
                closest = abs(sums[i] - sums[i - 1])
        result.sort()

        return result[0] + 1, result[1]