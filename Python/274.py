June 18, 2020

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # binary search a  
        citations.sort()
        n = len(citations)
        for i, num in enumerate(citations):
            if num >= n - i:
                return n - i
        return 0
            
            
            