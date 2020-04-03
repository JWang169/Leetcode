# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False 
#         self.wordList = []
    
    
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # n words with length n
        prefix = self.buildprefix(words)
        self.res = []
        self.dfs([], len(words[0]), prefix)
        return self.res
    
    def dfs(self, path, size, prefix):
        if len(path) == size:
            self.res.append(path)
            return 
        
        row = len(path)
        head = ""
        for word in path:
            head += word[row]
        if head not in prefix:
            return 
        for nxt in prefix[head]:
            self.dfs(path + [nxt], size, prefix)
        return 
        
        
    
    def buildprefix(self, words):
        prefix = collections.defaultdict(set)
        for word in words:
            for i in range(len(word) + 1):
                prefix[word[:i]].add(word)
        return prefix 
        
        