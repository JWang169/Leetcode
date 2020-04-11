# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nums = []
        while head:
            nums.append(head)
            head = head.getNext()
        for node in nums[::-1]:
            node.printValue()
        

# class Solution:
#     def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
#         nums = []
#         while head:
#             nums.append(head)
#             head = head.getNext()
#         while nums:
#             nums.pop().printValue()