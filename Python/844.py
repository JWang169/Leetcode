class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ps, pt = len(S) - 1, len(T) - 1
        countS, countT = 0, 0
        while ps >= 0 and pt >= 0:
            while ps >= 0 and countS >= 0:
                if S[ps] == '#':
                    countS += 1 
                    ps -= 1 
                elif countS > 0:
                    countS -= 1 
                    ps -= 1
                else:
                    break
            while pt >= 0 and countT >= 0:
                if T[pt] == '#':
                    countT += 1 
                    pt -= 1 
                elif countT > 0:
                    countT -= 1 
                    pt -= 1
                else:
                    break
            if pt >= 0 and ps >= 0 and T[pt] == S[ps]:
                ps -= 1
                pt -= 1
            else:
                break
        while ps >= 0 and countS >= 0:
            if S[ps] == '#':
                countS += 1 
                ps -= 1 
            elif countS > 0:
                countS -= 1 
                ps -= 1
            else:
                break
        while pt >= 0 and countT >= 0:
            if T[pt] == '#':
                countT += 1 
                pt -= 1 
            elif countT > 0:
                countT -= 1 
                pt -= 1
            else:
                break
        return pt == ps == -1
        
        
        