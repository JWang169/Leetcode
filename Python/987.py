# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        trees = dict()
        queue = deque([(root, 0)])
        while queue:
            level = []
            for i in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, index - 1))
                if node.right:
                    queue.append((node.right, index + 1))
                level.append((node.val, index))
            level.sort()
            for val, index in level:
                trees[index] = trees.get(index, [])
                trees[index].append(val)
        results = []
        for index in sorted(trees.keys()):
            results.append(trees[index])
        return results
        