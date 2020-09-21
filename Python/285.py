# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.nodes = list()
        self.dfs(root)
        for idx, node in enumerate(self.nodes):
            if node.val == p.val:
                if idx == len(self.nodes) - 1:
                    return None 
                return self.nodes[idx + 1]
        return None
    
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.nodes.append(node)
        self.dfs(node.right)

"""
别人家的方法：
如果cur_root比p大， 说明successor在左边或者就是cur_root. 
如果cur_root比p小，说明successor再右边

其实就是几种情况： 
1. root > p: root就是successor或者在左边
2. root < p: successor肯定在右边
3. root == p: successor在右边
"""
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None 
        if root.val > p.val:
            return self.inorderSuccessor(root.left, p) or root
        
        return self.inorderSuccessor(root.right, p)
        
        