class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        if divisor == 0:
            return 0

        
        neg = dividend > 0 and divisor < 0 or (dividend < 0 and divisor > 0)
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            shift = 0
            while a >= (b << shift):
                shift += 1 
            a -= b << (shift - 1)
            res += 2 ** (shift - 1)
            

        res = -res if neg else res 
        if res > INT_MAX:
            return INT_MAX
        return res