class Solution:
    def mySqrt(self, x: int) -> int:
        # if x <= 1 :
        #     return x
        left, right = 0, x 
        while left + 1 < right:
            mid = (left + right) // 2 
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
                
        return right if right * right <= x else left