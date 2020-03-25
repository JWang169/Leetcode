class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.overlap = False
        self.left = None
        self.right = None 
        
    
class MyCalendarTwo:

    def __init__(self):
        self.root = None
        
        
    def book(self, start: int, end: int) -> bool:
        if not self.valid(start, end, self.root):
            return False 
        
        self.root = self.insert(start, end, self.root)
        return True 
    
    def insert(self, start, end, root):
        if not root:
            root = TreeNode(start, end)
            return root
        
        if start >= end:
            return root
        
        if start >= root.end:
            root.right = self.insert(start, end, root.right)
            
        elif end <= root.start:
            root.left = self.insert(start, end, root.left)
            
        # overlap
        else:
            root.overlap = True 
            ns = min(start, root.start)
            rs = max(start, root.start)
            ne = max(end, root.end)
            re = min(end, root.end)
            root.start, root.end = rs, re
            root.left = self.insert(ns, rs, root.left)
            root.right = self.insert(re, ne, root.right)
        return root
        
        
    
    def valid(self, start, end, root):
        if start >= end:
            return True 
        if not root:
            return True 
        if start >= root.end:
            return self.valid(start, end, root.right)
        if end <= root.start:
            return self.valid(start, end, root.left)
        
        # overlap:
        if root.overlap:
            return False
        if start >= root.start and end <= root.end:
            return True 
        return self.valid(start, root.start, root.left) and self.valid(root.end, end, root.right)
        
                    
        
        
        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)