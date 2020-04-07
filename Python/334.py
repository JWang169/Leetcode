class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left, mid = sys.maxsize, sys.maxsize
        for n in nums:
            if n <= left:
                left = n
                continue
            elif n <= mid:
                mid = n
            else:
                return True 
            
        return False 