class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1 
                j += 1 
            elif name[i] != typed[j] and i > 0 and name[i - 1] == typed[j]:
                while j < len(typed) and name[i - 1] == typed[j]:
                    j += 1    
            else:
                break
        
        if i == len(name) and j < len(typed):
            while i > 0 and j < len(typed) and name[i - 1] == typed[j]:
                j += 1             
                
        if i == len(name) and j == len(typed):
            return True
        
        return False
            
        