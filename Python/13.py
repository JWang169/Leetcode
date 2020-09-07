class Solution:
    def romanToInt(self, s: str) -> int:
        pairs = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}   
        result = 0
        pre = 0
        for r in s[::-1]:
            cur = pairs[r]
            if cur < pre:
                result -= pairs[r]
            else:
                result += pairs[r]
            pre = pairs[r]
        return result