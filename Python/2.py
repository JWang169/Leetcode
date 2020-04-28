# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """      
        if not l2 and not l2:
            return None 
        
        result = 0 
        prev = 0
        weight = 1
        dummy = ListNode(0)
        head = dummy
        
        while l1 or l2 or prev:
            cur = prev
            if l1:
                cur += l1.val 
                l1 = l1.next
            if l2:
                cur += l2.val 
                l2 = l2.next 
            prev = cur // 10
            cur = cur % 10
            head.next = ListNode(cur)
            head = head.next
                
        if not dummy.next:
            return dummy
        return dummy.next 
        
        