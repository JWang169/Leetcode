# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        data = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if not node:
                data.append('#')
                continue
            data.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while data[-1] == '#':
            data.pop()
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None 
        root = TreeNode(data[0])
        queue = deque([root])
        idx = 1
        father = queue.popleft()
        while idx < len(data):
            leftVal = data[idx]
            if leftVal == '#':
                father.left = None
            else:
                father.left = TreeNode(leftVal)
                queue.append(father.left)
            idx += 1 
            if idx < len(data):
                rightVal = data[idx]
                if rightVal == '#':
                    father.right = None
                else:
                    father.right = TreeNode(rightVal)
                    queue.append(father.right)
                idx += 1 
            father = queue.popleft()

        return root
                
            
            
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))