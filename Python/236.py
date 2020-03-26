# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Mar 25
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val == q.val:
            return p
        self.lca = None 
        self.search(root, p, q)
        return self.lca
    
    
    def search(self, node, p, q):
        if not node:
            return False 
        left = self.search(node.left, p, q)
        right = self.search(node.right, p, q)
        if node.val == p.val or node.val == q.val:
            cur = True
        else:
            cur = False
        if not self.lca:
            if left and right:
                self.lca = node 
            if (left or right) and cur:
                self.lca = node
        
        return left or right or cur
            

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        self.result = None
        self.search(root, p, q)
        return self.result 
    
    def search(self, root, p, q):
        if not root:
            return None, None
        leftp, leftq = self.search(root.left, p, q)
        rightp, rightq = self.search(root.right, p, q)
        
        rootp = leftp or rightp or root.val == p.val
        rootq = leftq or rightq or root.val == q.val
        
        if not self.result and rootp and rootq:
            self.result = root
        
        return rootp, rootq