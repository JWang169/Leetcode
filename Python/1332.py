class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        
        left, right = 0, len(s) - 1 
        while left < right and s[left] == s[right]:
            left += 1 
            right -= 1 
        
        if left >= right:
            return 1 
        else:
            return 2