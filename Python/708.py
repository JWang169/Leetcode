"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newNode = Node(insertVal, head)
        if not head:
            newNode.next = newNode
            return newNode
        
        prev = head
        cur = head.next
        while 1:
            # 1. prev.val <= x <= head.val
            if prev.val <= insertVal <= cur.val:
                break         
            # 2. x is the max or min value => start or end position
            #     end => start
            elif prev.val > cur.val and (insertVal < cur.val or insertVal > prev.val):
                break
            prev = prev.next
            cur = cur.next
            
            # end circle 
            if prev == head:
                break
            
        prev.next = newNode
        newNode.next = cur
        return head
        