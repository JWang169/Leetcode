# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        self.seen = {}
        return self.dfs(1, n)
        
    
    
    def dfs(self, start, end):
        if start > end:
            return [None]
        
        if (start, end) in self.seen:
            return self.seen[(start, end)]      
        
        if start == end:
            node = TreeNode(start)
            self.seen[(start, end)] = [node] 
            return self.seen[(start, end)]      
            
        cur = []
        for i in range(start, end + 1):
            left = self.dfs(start, i - 1)
            right = self.dfs(i + 1, end)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    cur.append(node)
        self.seen[(start, end)] = cur
        return cur
        
        