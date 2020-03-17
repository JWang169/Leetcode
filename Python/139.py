class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False] * n 
        words = set(wordDict)
        
        # iterate start point
        for i in range(n):
            # iterate end point
            for j in range(i + 1, n + 1):
                if s[i: j] in words:
                    if i == 0:
                        f[j - 1] = True
                        continue
                    if f[i - 1]:
                        f[j - 1] = True
        return f[-1]