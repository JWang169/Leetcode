# memoization + dfs
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        memo = {}
        return [word for word in words if self.dfs(word, memo, words)]
    
    def dfs(self, word, memo, words):
        if word in memo:
            return memo[word]
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in words and suffix in words:
                memo[word] = True
                return True
            if prefix in words and self.dfs(suffix, memo, words):
                memo[word] = True
                return True 
            if suffix in words and self.dfs(prefix, memo, words):
                memo[word] = True
                return True
        return False 
    
# dp 
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        mappings = collections.defaultdict(set)
        for word in words:
            n = len(word)
            mappings[n].add(word)
            
        self.results = set()    
        for word in words:
            n = len(word)
            if n == 0:
                continue
            dp = [False] * (n + 1)
            dp[0] = True 
            for i in range(1, n + 1):
                for j in range(i):
                    length = i - j
                    if length in mappings and word[j:i] in mappings[length] and dp[j] and word[j : i] != word:
                    # if dp[j] and word[j : i] in words and word[j : i] != word:
                        dp[i] = True 
                        break
            if dp[-1]:
                self.results.add(word)
                
        return list(self.results)
        
    
        
        
        
        