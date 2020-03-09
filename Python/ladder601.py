from collections import deque 

class Vector2D(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.vec2d = vec2d 
        self.idx = -1
        self.queue = deque()

    # @return {int} a next element
    def next(self):
        # Write your code here
        return self.queue.popleft()
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        if len(self.queue) != 0:
            return True 
            
        self.idx += 1 
        while self.idx < len(self.vec2d) and len(self.vec2d[self.idx]) == 0:
            self.idx += 1 
            
        if self.idx == len(self.vec2d):
            return False     
            
        cur = self.vec2d[self.idx]
        self.queue = deque(cur)
        print(self.queue)
        return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())