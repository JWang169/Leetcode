# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return 
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        pre, post = pre[1:], post[:-1]
        i = post.index(pre[0])
        root.left = self.constructFromPrePost(pre[:i+1], post[: i+1])
        root.right = self.constructFromPrePost(pre[i+1:], post[i+1: ])
        return root