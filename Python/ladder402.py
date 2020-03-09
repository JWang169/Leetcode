import sys 
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        if not A:
            return []
        
        minSum, preSum = 0, 0
        maxSum = -sys.maxsize
        minIdx = -1
        left, right = -1, -1 
        for i, num in enumerate(A):
            preSum += num 
            if preSum - minSum > maxSum:
                maxSum = preSum - minSum
                left, right = minIdx + 1, i 
            if preSum < minSum:
                minSum = preSum
                minIdx = i
        return [left, right]