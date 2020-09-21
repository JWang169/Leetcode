# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # 1. get the total of the tree. 
        # 2. go through every possible subtree value. 
        MOL = 10 ** 9 + 7
        self.sums = []
        self.getSum(root)
        total = self.sums[-1]
        res = 0
        for num in self.sums[:-1]:
            res = max(res, num * (total - num))
        return res % MOL
    
    
    def getSum(self, node):
        if not node:
            return 0
        curSum = self.getSum(node.left) + self.getSum(node.right) + node.val
        self.sums.append(curSum)
        return curSum
        