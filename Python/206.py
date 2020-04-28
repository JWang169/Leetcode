# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev = None 
        while head:
            nxt = head.next 
            head.next = prev 
            prev = head
            head = nxt
        return prev 
            
        
        
# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head, None)
        
        
    def helper(self, head, prev):  
        if not head:
            return prev
        nxt = head.next
        head.next = prev
        return self.helper(nxt, head)
        
        
# iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
            
        
        
        