# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        targets = set(to_delete)
        if not root:
            return []
        queue = deque([[root, None]])
        newRoots = set()
        results = []
        left2root = dict()
        right2root = dict()
        while queue:
            node, prev = queue.popleft() 
            if prev == None and node.val not in targets:
                results.append(node)
            
            if node.val in targets:
                prev = None
                if node in left2root:
                    left2root[node].left = None
                if node in right2root:
                    right2root[node].right = None
            else:
                prev = node
                
            if node.left:
                left2root[node.left] = node
                queue.append([node.left, prev])
            if node.right:
                right2root[node.right] = node
                queue.append([node.right, prev])
                
        return results
                