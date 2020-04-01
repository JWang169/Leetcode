# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        subhead = dummy
        for i in range(1, m):
            subhead = subhead.next # i=1, subhead=1...
        
        # subhead = m - 1
        prevM = subhead # 1

        subhead = subhead.next # 2
        nxt = subhead.next # 3
        for i in range(n - m):
            temp = nxt.next # 4
            nxt.next = subhead # 3 -> 2
            subhead = nxt
            nxt = temp
        prevM.next.next = nxt
        prevM.next = subhead
        return dummy.next
            
        