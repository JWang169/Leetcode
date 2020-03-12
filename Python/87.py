class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False 
        n = len(s1)
        # if length < 3, s1 can swap to s2
        if n <= 3:  
            return True 
        
        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
               self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True
        return False
            