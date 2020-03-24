# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return 
        dummy = ListNode(-sys.maxsize)
        while head:
            nxt = head.next
            cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next 
            head.next = cur.next
            cur.next = head
            head = nxt
        return dummy.next