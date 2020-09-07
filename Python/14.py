class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        idx = 0
        while True:
            for s in strs:
                if not s or len(s) == idx or s[idx] != strs[0][idx]:
                    return strs[0][:idx] if idx > 0 else ""
            idx += 1
        return strs[0][:idx]
        
        
        