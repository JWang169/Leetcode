# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        word = wordlist[0]
        words = set(wordlist)
        while words:
            count = master.guess(word)
            nxt = []
            if count == 6:
                return word 
            for w in words:
                score = self.match(word, w)
                if score == count:
                    nxt.append(w)
            words = nxt
            word = words.pop()
        
            
    def match(self, w1, w2):
        score = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                score += 1 
        return score 
            
        