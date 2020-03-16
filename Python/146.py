class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.cache = dict()
        self.heap = []
        self.step = 0
        self.visited_times = dict()
        self.capacity = capacity
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key in self.cache:
            self.step += 1 
            heapq.heappush(self.heap, (self.step, key))
            self.visited_times[key] = self.visited_times.get(key, 0) + 1 
            return self.cache[key]
            
        return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def put(self, key, value):
        # write your code here
        self.step += 1 
        if key in self.cache or len(self.cache) < self.capacity:
            self.update(key, value)
            return
            
        if len(self.cache) == self.capacity:
            self.remove()
            self.update(key, value)
            return
            
    def update(self, key, value):
        heapq.heappush(self.heap, (self.step, key))
        self.visited_times[key] = self.visited_times.get(key, 0) + 1  
        self.cache[key] = value
    
    def remove(self):
        while len(self.heap) >0:
            _, key = heapq.heappop(self.heap)
            self.visited_times[key] -= 1 
            if self.visited_times[key] == 0:
                del self.cache[key]
                return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)