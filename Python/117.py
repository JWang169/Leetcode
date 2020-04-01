"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# O(1) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        start = root
        while root:
            dummy = Node(0)
            prev = dummy
            while root:
                if root.left:
                    prev.next = root.left
                    prev = prev.next
                if root.right:
                    prev.next = root.right
                    prev = prev.next
                root = root.next
            root = dummy.next
        return start
        
        



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None 
        queue = deque([root])
        
        while queue:
            prev = None 
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if not prev:
                    prev = cur
                    continue
                else:
                    prev.next = cur
                    prev = cur 
        return root 
        
        