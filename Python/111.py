# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        count = 0
        while queue:
            count += 1 
            for i in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return count 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count 