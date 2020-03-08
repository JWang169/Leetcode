class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        mappings = {}
        preSum = 0
        mappings[0] = -1
        for i in range(len(nums)):
            cur = preSum + nums[i]
            preSum = cur
            if cur in mappings:
                return mappings[cur] + 1, i
            mappings[cur] = i
            
        return -1, -1