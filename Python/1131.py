class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0
        n = len(arr1)
        dirs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for x, y in dirs:
            right = x * arr1[0] + y * arr2[0] + 0
            for i in range(n):
                left = x * arr1[i] + y * arr2[i] + i
                result = max(result, left - right)
                right = min(left, right)
        
        return result