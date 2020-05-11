class LFUCache:

    def __init__(self, capacity: int):
        self.history = dict()
        self.heap = list()
        self.capacity = capacity
        self.seq = 0
        

    def get(self, key: int) -> int:
        if key not in self.history or self.capacity < 1:
            return -1
        
        self.seq += 1 
        self.history[key][1] += 1
        count = self.history[key][1]
        heapq.heappush(self.heap, (count, self.seq, key))
        # print(self.heap)
        return self.history[key][0]
        

    def put(self, key: int, value: int) -> None:
        if len(self.history) == self.capacity and key not in self.history:
            while self.heap:
                freq, seq, num = heapq.heappop(self.heap)
                if self.history[num][1] == freq:
                    del self.history[num]
                    break
                    
        self.seq += 1 
        if key not in self.history:
            self.history[key] = [value, 1]
            heapq.heappush(self.heap, (1, self.seq, key))
        else:
            val, count = self.history[key]
            self.history[key] = [value, count + 1]
            heapq.heappush(self.heap, (self.history[key][1], self.seq, key))
            
        
        # print(self.history)
        # print(self.heap)
    
        return 
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)