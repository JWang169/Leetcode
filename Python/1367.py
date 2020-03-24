# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
# space: O(n), n is the amount of nodes 
# time: O(n * m), n is the amount of tree nodes, m is the length of the linked list
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False 
        queue = deque()
        qTree = deque([root])
        while qTree:
            node = qTree.popleft()
            if node.left:
                qTree.append(node.left)
            if node.right:
                qTree.append(node.right)
            if node.val == head.val:
                queue.append(node)
                
        
        while queue and head:
            head = head.next
            if not head:
                break
            target = head.val
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left and node.left.val == target:
                    queue.append(node.left)
                if node.right and node.right.val == target:
                    queue.append(node.right)
        return not head