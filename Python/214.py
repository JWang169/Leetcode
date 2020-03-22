class Solution:
    def shortestPalindrome(self, s: str) -> str:
        double = s + '*' + s[::-1]
        lps = self.longestPrefixString(double)
        index = lps[-1]
        return s[index: ][::-1] + s
        
    
    def longestPrefixString(self, s):
        lps = [0] * len(s)
        i, j = 0, 1
        while j < len(s):
            if s[i] == s[j]:
                lps[j] = i + 1
                i += 1 
                j += 1 
            else:
                if i == 0:
                    j += 1 
                else:
                    i = lps[i - 1]
        return lps