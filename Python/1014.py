class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        first, second = -sys.maxsize, 0
        for i, num in enumerate(A):
            second = max(second, num - i + first)
            first = max(first, num + i)
        
        return second
        
            
        
        