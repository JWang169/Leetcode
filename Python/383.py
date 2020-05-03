class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for ch in magazine:
            mag[ch] = mag.get(ch, 0) + 1
        
        for ch in ransomNote:
            if ch not in mag:
                return False
            mag[ch] -= 1 
            if mag[ch] == 0:
                del mag[ch]
        return True 
        
        
        
        