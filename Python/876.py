# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head 
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        if not fast:
            return slow
        return slow.next