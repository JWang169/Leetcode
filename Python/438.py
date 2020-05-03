class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cur = Counter(p)
        start = 0
        results = []
        
        for i, ch in enumerate(s):
            if ch not in cur:
                cur = Counter(p)
                start = i + 1
                continue
                
            while ch in cur and cur[ch] == 0:
                cur[s[start]] += 1
                start += 1 
                 
            cur[ch] -= 1 
            if cur[ch] == 0 and i - start + 1 == len(p):
                results.append(start)
                cur[s[start]] += 1
                start += 1 
                
        return results
        
        