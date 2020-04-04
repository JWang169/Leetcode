class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False 
        if len(s) == k:
            return True 
        letters = collections.Counter(s)
        mid = []
        for key, val in letters.items():
            if val % 2 == 1:
                mid.append(key)
        if len(mid) > k:
            return False
        return True 
        