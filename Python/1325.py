# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None 
        
        queue = deque()
        dummy = TreeNode(0)
        dummy.left = root
        parents = dict() # [parent, isLeft(True/False)]
        queue.append(root)
        parents[root] = [dummy, True]
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if not cur.left and not cur.right and cur.val == target:
                    if cur in parents:
                        parent, isLeft = parents[cur]
                        if isLeft:
                            parent.left = None
                        else:
                            parent.right = None
                        queue.append(parent)
                if cur.left:
                    parents[cur.left] = [cur, True]
                    queue.append(cur.left)
                if cur.right:
                    parents[cur.right] = [cur, False]
                    queue.append(cur.right)
        return dummy.left        