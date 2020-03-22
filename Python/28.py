class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return 0 if len(needle) == 0 else -1
        
        pattern = [0] * (len(needle))
        i, j = 0, 1
        # build lps table
        
        while j < len(needle):
            target = needle[i]
            if needle[j] == target:
                pattern[j] = i + 1
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1 
                else:
                    i = pattern[i - 1]
        i, idx = 0, 0
        while i < len(haystack) and idx < len(pattern):
            if haystack[i] == needle[idx]:
                idx += 1
                i += 1
            else:
                if idx == 0:
                    i += 1
                else:
                    idx = pattern[idx - 1]        
            if idx == len(needle):
                return i - idx
            
        return -1
                    
                    
        