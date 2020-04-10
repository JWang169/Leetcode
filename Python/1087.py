class Solution:
    def expand(self, S: str) -> List[str]:
        return sorted(self.dfs(S, ['']))
                
    
    def dfs(self, s, prev):
        if not s:
            return prev
        n = len(s)
        cur = ''
        found = False 
        result = []
        for i in range(n):
            if s[i].isalpha():
                cur += s[i]
                continue
            if s[i] == '{':
                found = True
                start = i
                break
        
        added = []    
        for sub in prev:
            added.append(sub + cur)
        if not found:
            return added
        
        end = s.find('}')
        chars = s[start + 1: end].split(',')
        arr = []
        for sub in added:
            for ch in chars:
                arr.append(sub + ch)
        
        # print(s[end + 1: ])
        return self.dfs(s[end + 1: ], arr)
        
            
        
        
        