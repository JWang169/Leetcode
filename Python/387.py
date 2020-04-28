class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = dict()
        for ch in s:
            ss[ch] = ss.get(ch, 0) + 1
        
        for ch in t:
            if ch not in ss:
                return False 
            ss[ch] -= 1 
            if ss[ch] == 0:
                del ss[ch]
                
        return len(ss) == 0

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = dict()
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1 
        for idx, ch in enumerate(s):
            if seen[ch] == 1:
                return idx
        return -1