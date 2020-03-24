# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # left right root
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
        # Do not cheat. Do Morris
        # link to the most left of current.right
        result = []
        while root:
            if root.right:
                prev = root.right
                while prev.left and prev.left != root:
                    prev = prev.left
                    
                if prev.left:
                    root = root.left
                else:
                    result.append(root.val)
                    prev.left = root
                    root = root.right
            else:
                result.append(root.val)
                root = root.left
        return result[::-1]