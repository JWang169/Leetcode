# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                # predecessor.right == current, meaning we're going back to the root

                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    predecessor.right = None
                    result.append(root.val)
                    root = root.right
                    
        return result