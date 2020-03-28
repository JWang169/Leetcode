class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False 
        if str1 == str2:
            return True 
        mappings = {}
        for i in range(len(str1)):
            c1, c2 = str1[i], str2[i]
            mappings[c1] = mappings.get(c1, c2)
            if mappings[c1] != c2:
                return False 
        return len(set(str2)) < 26
            
        
        