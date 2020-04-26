from collections import deque
class WebLogger:
    
    def __init__(self):
        self.times = deque()


    """
    @param: timestamp: An integer
    @return: nothing
    """
    def hit(self, timestamp):
        self.times.append(timestamp)
        while self.times and self.times[0] + 300 <= timestamp:
            self.times.popleft()
        

    """
    @param: timestamp: An integer
    @return: An integer
    """
    def get_hit_count_in_last_5_minutes(self, timestamp):
        while self.times and self.times[0] + 300 <= timestamp:
            self.times.popleft()
        return len(self.times)
        
        
        