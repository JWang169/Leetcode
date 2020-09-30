class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        left, right, res = 0, 0, 0
        seen = set()
        mapping = dict()
        while right < len(s):
            mapping[s[right]] = right            
            if s[right] not in seen and len(seen) == 2:
                while left < right:
                    if mapping[s[left]] == left:
                        del mapping[s[left]]
                        seen.remove(s[left])
                        left += 1 
                        break
                    else:
                        left += 1 
            seen.add(s[right])
            res = max(res, right - left + 1)
            right += 1   
            
        return res 