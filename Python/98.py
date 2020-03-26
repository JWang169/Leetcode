# Mar 25
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        isBST, mi, ma = self.helper(root)
        return isBST
        
    
    def helper(self, root):
        # @return isBST, min, max 
        if not root:
            return True, None, None
        
        leftBST, leftMin, leftMax = self.helper(root.left)
        rightBST, rightMin, rightMax = self.helper(root.right)
        if not leftMax:
            leftMax = -sys.maxsize
        if not rightMin:
            rightMin = sys.maxsize 
        
        if leftBST and rightBST and leftMax < root.val < rightMin:
            isBST = True 
        else:
            isBST = False 
        
        mi = leftMin if leftMin else root.val 
        ma = rightMax if rightMax else root.val
        
        return isBST, mi, ma
            
        


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.isValid = True
        self.helper(root)
        return self.isValid
        
        
    def helper(self, root):
        if not root:
            # min child, max child
            return None, None
        
        lmin, lmax = self.helper(root.left)
        rmin, rmax = self.helper(root.right)
        if lmax and root.val <= lmax:
            self.isValid = False
            return None, None 
        if rmin and root.val >= rmin:
            self.isValid = False
            return None, None
        
        mi = lmin if lmin else root.val 
        ma = rmax if rmax else root.val 
        return mi, ma