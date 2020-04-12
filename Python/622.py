# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([[root, 0]])
        ma = 0
        while queue:
            first, last = queue[0][1], queue[-1][1]
            ma = max(ma, last - first + 1)
            for i in range(len(queue)):
                node, idx = queue.popleft()
                if node.left:
                    queue.append([node.left, idx * 2])
                if node.right:
                    queue.append([node.right, idx * 2 + 1])
        return ma 