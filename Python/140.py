# April 14
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.seen = dict()
        words = set(wordDict)
        self.dfs(s, words)
        return self.seen[s]
        
    
    def dfs(self, s, words):
        if not s:
            return []
        if s in self.seen:
            return self.seen[s]
        
        cur = []
        for i in range(1, len(s) + 1):
            if s[:i] in words:
                nexts = self.dfs(s[i:], words)
                for nxt in nexts:
                    cur.append(s[:i] + ' ' + nxt)
        
        if s in words:
            cur.append(s)
        
        self.seen[s] = cur
        return cur
        
        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # memo = {}
        return self.dfs(s, wordSet, {})
    
    
    def dfs(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return []
        
        partitions = []
                    
        for i in range(1, len(s) + 1):
            if s[:i] not in wordSet:
                continue 
            subPartitions = self.dfs(s[i:], wordSet, memo)
            for sub in subPartitions:
                partitions.append(s[:i] + ' ' + sub)
        
        if s in wordSet:
            partitions.append(s)
            
        memo[s] = partitions
        return partitions



"""
介绍一种TLE... shame Joey
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.results = []
        self.wordSet = set(wordDict)
        self.partition(s, '')
        return self.results
    
    
    def partition(self, s, paths):
        if not s and paths:
            self.results.append(paths)
            return
        
        for i in range(1, len(s) + 1):
            if s[:i] in self.wordSet:
                if len(paths) > 0:
                    self.partition(s[i:], paths + ' ' + s[:i])
                else:
                    self.partition(s[i:], paths + s[:i])
        return 
"""