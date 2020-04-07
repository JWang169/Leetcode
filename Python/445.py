# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        num1 = 0
        num2 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num = num1 + num2
        if num == 0:
            return ListNode(0)
        nums = []
        while num:
            nums.append(num % 10)
            num = num // 10
        
        nums.reverse()
        head = dummy
        for num in nums:
            node = ListNode(num)
            head.next = node
            head = head.next
        return dummy.next
            
        
        
        
        