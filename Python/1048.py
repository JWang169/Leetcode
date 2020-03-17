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