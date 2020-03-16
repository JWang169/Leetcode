class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = dict()
        for ch in s:
            seen[ch] = seen.get(ch, 0) + 1 
        for idx, ch in enumerate(s):
            if seen[ch] == 1:
                return idx
        return -1