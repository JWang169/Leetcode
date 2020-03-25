class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicts = collections.Counter(s)
        for ch in t:
            if ch not in dicts or dicts[ch] == 0:
                return ch
            dicts[ch] -= 1
        return ""
        