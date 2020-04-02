class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # divide and conquer 
        if len(s) < k:
            return 0
        counter = collections.Counter(s)
        longest = 0
        prev = 0
        found = False 
        for i, ch in enumerate(s):
            if counter[ch] < k:
                length = self.longestSubstring(s[prev: i], k)
                longest = max(length, longest)
                prev = i + 1
                found = True 
        if not found:
            return len(s)
        else:
            return max(self.longestSubstring(s[prev:], k), longest)
        
        