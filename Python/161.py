class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        edit = False
        ps, pt = 0, 0
        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1 
                pt += 1  
            
            elif edit:
                return False 
            
            elif len(s) > len(t):
                ps += 1 
                edit = True 
            
            elif len(s) < len(t):
                pt += 1 
                edit = True  
            
            elif len(s) == len(t):
                pt += 1 
                ps += 1 
                edit = True                 
        
        if not edit:
            if ps < len(s):
                edit = True
                ps += 1 
            elif pt < len(t):
                edit = True
                pt += 1 
        return ps == len(s) and pt == len(t) and edit
        
        