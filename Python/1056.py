class Solution:
    def confusingNumber(self, N: int) -> bool:
        mappings = {0:0, 1:1, 6:9, 8:8, 9:6}
        num = N
        rotate = 0
        while num > 0:
            n = num % 10
            if n not in mappings:
                return False 
            rotate = rotate * 10 + mappings[n]
            num = num // 10
        return rotate != N 