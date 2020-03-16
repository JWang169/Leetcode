# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        heap = []
        for index, headNode in enumerate(lists):
            if not headNode:
                continue
            heapq.heappush(heap, (headNode.val, index))
        dummy = ListNode(-1)
        head = dummy
        while heap:
            nodeVal, index = heapq.heappop(heap)
            node = lists[index]
            head.next = node
            head = head.next 
            if node.next:
                node = node.next 
                heapq.heappush(heap, (node.val, index))
                lists[index] = node

        return dummy.next 