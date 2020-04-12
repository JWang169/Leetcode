class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = 0
        n = N
        while n > 0:
            k += 1 
            n //= 10
        
        n = N
        arm = 0
        while n > 0:
            remain = n % 10
            arm += remain ** k
            n //= 10
        return arm == N
        
        