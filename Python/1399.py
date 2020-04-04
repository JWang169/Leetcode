class Solution:
    def countLargestGroup(self, n: int) -> int:
        digits = dict()
        ma = 0
        for i in range(1, n + 1):
            s = 0
            while i > 0:
                s += i % 10
                i = i // 10
            digits[s] = digits.get(s, 0) + 1
            ma = max(ma, digits[s])
        
        result = 0
        for key, val in digits.items():
            if val == ma:
                result += 1 
        return result 
        