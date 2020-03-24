# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # there are two nodes to find 
        self.nodes = []
        self.inorder(root)
        t1, t2 = None, None
        for i in range(len(self.nodes) - 1):
            if self.nodes[i + 1] < self.nodes[i]:
                t1 = self.nodes[i + 1]
                if t2 == None:  
                    t2 = self.nodes[i]
                else:
                    break
        self.search(t1, t2, root, 2)
        return root
        
        
    def search(self, t1, t2, root, count):
        if not root:
            return
        if root.val == t1 and count > 0:
            root.val = t2
            count -= 1
        elif root.val == t2 and count > 0:
            root.val = t1
            count -= 1
        if count == 0:
            return
        self.search(t1, t2, root.left, count)
        self.search(t1, t2, root.right, count)
        
        
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        self.nodes.append(root.val)
        self.inorder(root.right)
        
        
        
        