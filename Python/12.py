"""
June 18, 2020. 
Get used to zip
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        result = ""
        for v, n in zip(values, nums):
            result += (num // v) * n
            num %= v
        
        return result 