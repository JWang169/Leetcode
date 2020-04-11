class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        # 求(A[i] + A[j] + i - j)的最大值，=> A[i] + i + A[j] - j 
        # A[i] + i可以随着i每次更新，max(prev, A[i] + i)， 
        # A[j] - j + prev 要先更新，因为j > i
        
        first, second = -sys.maxsize, 0
        for i, num in enumerate(A):
            second = max(second, num - i + first)
            first = max(first, num + i)
        
        return second