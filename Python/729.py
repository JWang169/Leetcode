class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
        
class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.search(start, end, self.root)
        
        
    def search(self, start, end, prev):            
        while prev:
            if start >= prev.end:
                if not prev.right:
                    node = Node(start, end)
                    prev.right = node
                    return True
                else:
                    return self.search(start, end, prev.right)
            if end <= prev.start:
                if not prev.left:
                    node = Node(start, end)
                    prev.left = node
                    return True
                else:
                    return self.search(start, end, prev.left)
            else:
                return False 
        
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)