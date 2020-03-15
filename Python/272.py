# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if not root:
            return []
        self.values = []
        self.inorder(root)
        left, right = 0, len(self.values) - 1
        # binary search
        while left + 1 < right:
            mid = (left + right) // 2 
            if self.values[mid] == target:
                left = mid 
                break
            if self.values[mid] < target:
                left = mid 
            else:
                right = mid
        if abs(self.values[left] - target) <= abs(self.values[right] - target):
            index = left
        else:
            index = right
        
        left, right = index - 1, index + 1
        results = [self.values[index]]
        count = 1
        while count < k:
            if left < 0:
                results.append(self.values[right])
                right += 1 
                count += 1 
                continue
            if right >= len(self.values):
                results.append(self.values[left])
                left -= 1 
                count += 1 
                continue 
            if abs(self.values[left] - target ) <= abs(self.values[right] - target):
                results.append(self.values[left])
                left -= 1
            else:
                results.append(self.values[right])
                right += 1 
            count += 1 
        return results
            
    
    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        self.values.append(root.val)
        self.inorder(root.right)