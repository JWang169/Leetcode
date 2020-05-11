class Solution:
    def isNumber(self, s: str) -> bool:
        hasDot = False
        hasNum = False
        hasE = False
        s = s.strip()
        for i, ch in enumerate(s):
            if ch == '-' or ch == '+':
                if i != 0 and s[i - 1] != 'e':
                    return False
                continue
            if ch == '.':
                if hasDot or hasE:
                    return False
                hasDot = True 
                continue 
            if ch == 'e':
                if not hasNum or hasE:
                    return False 
                hasNum = False
                hasE = True 
                continue 
            if ch.isdigit():
                hasNum = True
            else:
                return False 
        return hasNum
        