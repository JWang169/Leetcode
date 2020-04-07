# 这题会了
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words or not words[0]:
            return 0
        result = 1
        self.seen = {}
        mappings = collections.defaultdict(set)
        for word in words:
            mappings[len(word)].add(word)
        # lens = sorted(list(mappings.keys()), reverse=True)
        for word in words:
            cur = self.dfs(word, mappings)
            result = max(cur, result)
        return result 
    
    
    def dfs(self, word, mappings):
        if word in self.seen:
            return self.seen[word]
        n = len(word)
        if n - 1 not in mappings:
            self.seen[word] = 1
            return 1
        nexts = mappings[n - 1]
        res = []
        for nxt in nexts:
            for i in range(len(word)):
                if word[:i] + word[i + 1:] == nxt:
                    cur = 1 + self.dfs(nxt, mappings)
                    res.append(cur)
        if not res:
            self.seen[word] = 1
            return 1
        
        self.seen[word] = max(res)
        return self.seen[word]
        

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lenWord = dict()
        for word in words:
            length = len(word)
            lenWord[length] = lenWord.get(length, set())
            lenWord[length].add(word)
        

        self.result = 1
        for word in words:
            self.search(lenWord, word, 1)
        return self.result
    
    def search(self, lenWord, word, count):       
        length = len(word)
        if length - 1 not in lenWord:
            return 
        for i in range(len(word)):
            if word[:i] + word[i + 1:] in lenWord[length - 1]:
                self.result = max(self.result, count + 1)
                self.search(lenWord, word[:i] + word[i + 1:], count + 1)
        return 