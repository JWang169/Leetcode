class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        self.total = 0
        self.left = None 
        self.right = None 
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self.buildTree(nums, 0, len(nums) - 1)
        
    def buildTree(self, nums, left, right):
        if left > right:
            return None
        if left == right:  # this is the leaf node, no furthur partition
            node = Node(left, right)
            node.total = nums[left]
            return node 
        mid = (left + right) // 2
        root = Node(left, right)
        root.left = self.buildTree(nums, left, mid)
        root.right = self.buildTree(nums, mid + 1, right)
        
        root.total = root.left.total + root.right.total 
        return root 
        

    def update(self, i: int, val: int) -> None:
        self.updateTree(self.root, i, val)
    
    def updateTree(self, root, i, val):
        """
        find root_i(a leaf note) and update its total to val. 
        root.left == root.right == i
        """
        if root.start == root.end:
            root.total = val 
            return val
        
        mid = (root.start + root.end) // 2 
        
        if i <= mid:  # if the idx is less than mid, the leaf node must be on the left of the current root
            self.updateTree(root.left, i, val)
        else:
            self.updateTree(root.right, i, val)
        
        # update the total of each passed root
        root.total = root.left.total + root.right.total 
        return root.total
         
    def sumRange(self, i: int, j: int) -> int:
        
        return self.getSum(self.root, i, j)
    
    def getSum(self, root, i, j):
        if root.start == i and root.end == j:
            return root.total
        mid = (root.start + root.end) // 2 
        if j <= mid:
            return self.getSum(root.left, i, j)
        if i >= mid + 1:
            return self.getSum(root.right, i, j)
        return self.getSum(root.left, i, mid) + self.getSum(root.right, mid + 1, j)
        
    
    
"""
build: O(n)
update: O(logn)
rangeQuery: O(logn + k)  k is the number of reported segments

"""