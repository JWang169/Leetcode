"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        while queue:
            queue.append(None)
            for i in range(len(queue) - 1):
                cur = queue.popleft()
                cur.next = queue[0]

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            queue.popleft()
        return root
                
            
            
        
        
        
        
        