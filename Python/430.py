# Apr 21 

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur, stack = head, []
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child 
                cur.child.prev = cur
                cur.child = None
            if not cur.next and stack:
                newNext = stack.pop()
                cur.next = newNext
                newNext.prev = cur
            
            cur = cur.next 
        
        return head
        
        
        

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur, stack = head, []
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child 
                cur.child.prev = cur
                cur.child = None
            if not cur.next and len(stack) > 0:
                newNext = stack.pop()
                newNext.prev = cur
                cur.next = newNext
            cur = cur.next 
            
        return head 