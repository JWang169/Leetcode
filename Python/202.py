class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False 
            seen.add(n)
            n = self.squares(n)
        return True
    
    def squares(self, n):
        s = 0
        while n:
            s += (n % 10) ** 2
            n = n // 10
        return s 
        
        
        