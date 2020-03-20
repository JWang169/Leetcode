class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if self.express(S, word):
                count += 1 
        return count 
            
    
    
    def express(self, S, word):
        j = 0
        for i in range(len(S)):
            if j < len(word) and S[i] == word[j]:
                j += 1 
                continue
            # S[i] != word[j]
            # xxi, xix, ixx
            if S[i - 2 : i + 1] != S[i] * 3 and S[i - 1: i + 2] != S[i] * 3:
                return False 
        return j == len(word)