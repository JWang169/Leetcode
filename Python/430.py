"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
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