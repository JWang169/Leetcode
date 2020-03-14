class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x >= 1:
            left, right = 0, x 
        else:
            left, right = 0, 1
            
        while left + 1e-10 < right:
            mid = (left + right) / 2 
            if mid * mid > x:
                right = mid 
            else:
                left = mid
        return left if (left * left - x) <= (right * right - x) else right