# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# fast/slow pointers
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head.next
        
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        
        if not fast or not fast.next:
            return None
        # slow, fast somewhere in the circle
        slow = slow.next
        while head != slow:
            head = head.next
            slow = slow.next
        return slow 
    






# set
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # hashmap 
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return None