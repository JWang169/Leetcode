class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            neg = -1
        else:
            neg = 1
        
        s = str(abs(x))
        num = int(s[::-1])
        if num > 2 ** 31 - 1:
            return 0
        return neg * int(s[::-1])
        