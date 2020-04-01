# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        nodeA = headA
        nodeB = headB
        while nodeA:
            nodeA = nodeA.next
            lenA += 1 
        while nodeB:
            nodeB = nodeB.next
            lenB += 1
        
        
        # headA is longer
        if lenA < lenB:
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA            
        for i in range(lenA - lenB):
            headA = headA.next
        
        meet = None 
        while headA:
            if headA == headB:
                meet = headA
                break
            headA = headA.next
            headB = headB.next
        return meet