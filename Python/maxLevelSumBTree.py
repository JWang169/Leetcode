# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 1
        que = deque()
        que.append(root)
        result = 1
        maxSum = root.val
        curLevel = 0
        while que:
            curLevel += 1 
            levelSum = 0
            for i in range(len(que)):
                node = que.popleft()
                levelSum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            if levelSum > maxSum:
                result = curLevel
                maxSum = levelSum
        return result