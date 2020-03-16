class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self.dfs(pattern, str, dict(), set())

    
    def dfs(self, pattern, str, mappings, subStr):
        if not pattern:
            return not str
        
        if pattern[0] in mappings:
            curStr = mappings[pattern[0]]
            if str[:len(curStr)] == curStr:
                return self.dfs(pattern[1:], str[len(curStr):], mappings, subStr)
            else:
                return False 
        
        for i in range(len(str)):
            sub = str[:i + 1]
            if sub in subStr:
                continue 
            mappings[pattern[0]] = sub 
            subStr.add(sub)
            if self.dfs(pattern[1:], str[len(sub):], mappings, subStr):
                return True 
            del mappings[pattern[0]]
            subStr.remove(sub)
        return False 
            
