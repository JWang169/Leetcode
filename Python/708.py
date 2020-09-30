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
"""
Sep. 22, 2020
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node 
        
        prev, cur = head, head.next
        while cur != head:
            if cur.val == insertVal or prev.val == insertVal:
                prev.next = node
                node.next = cur
                return head
            
            # increasing: prev.val < cur.val
            if prev.val <= cur.val:
                if insertVal < prev.val or insertVal > cur.val:
                    prev = cur
                    cur = cur.next 
                elif prev.val < insertVal < cur.val:
                    prev.next = node
                    node.next = cur
                    return head
            else: # prev.val > cur.val, end of increasing
                if insertVal > prev.val or insertVal < cur.val:
                    prev.next = node
                    node.next = cur
                    return head                  
                else:
                    prev = cur
                    cur = cur.next 
        prev.next = node
        node.next = cur
        return head
