class Solution:
    def longestPrefix(self, s: str) -> str:
        if len(s) == 1:
            return ""
        
        lps = [0] * len(s)
        i, j = 0, 1
        while j < len(s):
            target = s[i]
            if s[j] == target:
                lps[j] = i + 1
                i += 1
                j += 1 
            else:
                if i != 0:
                    i = lps[i - 1]
                else:
                    j += 1 
        if lps[-1] == 0:
            return ""
        return s[len(s) - lps[-1]:]

        