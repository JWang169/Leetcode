# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        return self.searchLevel(S, 1)
    
    def searchLevel(self, S, level):
        if not S:
            return None
        start = 0
        # find the first dash
        while start < len(S) and S[start] != '-':
            start += 1 

        rootVal = int(S[:start])
        root = TreeNode(rootVal)
        
        # no dash found => leaf node, no children
        if start == len(S):
            return root
        
        # start + level is the index of leftnode
        leftIndex = start + level
        
        # search for right node 
        count = 0
        rightIndex = -1
        for i in range(leftIndex, len(S)):
            if S[i] == '-':
                count += 1 
            else:
                if count == level:
                    rightIndex = i 
                    break
                else:
                    count = 0         
        
        # no right found
        if rightIndex == -1:
            root.left = self.searchLevel(S[leftIndex: ], level + 1)
            return root
        else:
            # with left and right
            root.left = self.searchLevel(S[leftIndex: rightIndex - level], level + 1)
            root.right = self.searchLevel(S[rightIndex: ], level + 1)
            return root

        
        