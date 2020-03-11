"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # 单调递减栈
        
        if not A:
            return None 

        # 因为是单调递减栈，所以最后要append一个超级大的值，保证在最后把stack里的都pop出去， 和单调递增栈最后append一个-1是一个道理
        nodes = [TreeNode(num) for num in A + [sys.maxsize]]
        stack = []
        for index, num in enumerate(A + [sys.maxsize]):
            while stack and A[stack[-1]] < num:
                top = stack.pop()
                # top的root是min(左边第一个比他大的， 右边第一个比他大的)
                left = A[stack[-1]] if stack else sys.maxsize
                if left < num:
                    nodes[stack[-1]].right = nodes[top]
                else:
                    nodes[index].left = nodes[top]
                    
            stack.append(index)
            
        return nodes[-1].left 