from collections import deque
import heapq
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.idx = -1
        self.queue = deque([_ for _ in range(len(sentences))])
        self.sentences = sentences
        self.times = times
        self.newSentence = ""
        
            
    def input(self, c: str) -> List[str]:
        self.idx += 1 
        if c == '#':
            self.idx = -1
            self.add()
            self.queue = deque([_ for _ in range(len(self.sentences))])
            self.newSentence = ""
            return []
        
        self.newSentence += c
        return self.search(c, self.idx)
        
    def add(self):
        while len(self.queue) > 0:
            item = self.queue.popleft()
            sen = self.sentences[item]
            if sen == self.newSentence:
                self.times[item] += 1 
                return
        self.sentences.append(self.newSentence)
        self.times.append(1)    
        return 
        
    def search(self, c, idx):
        candis = []
        for _ in range(len(self.queue)):       
            item = self.queue.popleft()
            sen = self.sentences[item]
            if len(sen) <= idx:
                continue
            if sen[idx] == c:
                heapq.heappush(candis, (-self.times[item], sen))
                self.queue.append(item)
        results = [] 
        for i in range(3):
            if len(candis) > 0:
                results.append(heapq.heappop(candis)[1])
            else:
                break
        return results
    
    

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)