from collections import deque
class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.counter = 0
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.check(timestamp)  
        self.queue.append(timestamp)
        self.counter += 1 

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.check(timestamp)
        return self.counter
        

    def check(self, timestamp: int) -> int:
        while self.queue and self.queue[0] + 300 <= timestamp:
            self.queue.popleft()
            self.counter -= 1
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)