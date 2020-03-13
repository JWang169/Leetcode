class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
        res = 1 
        for n in b:
            res = pow(res, 10) * pow(a, n) % 1337
        return res
    
    def pow(x, n):
        if n == 0:
            return 1
        return pow(x % 1337, n // 2) * pow(x % 1337, n - n // 2) % 1337