class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        m, n = len(A), len(A[0])
        for i in range(1, m - 1):
            left, right = 0, n - 1
            while left + 1 < right:
                mid = (left + right) // 2 
                if A[i][mid] > A[i][mid - 1] and A[i][mid] > A[i][mid + 1]:
                    break
                elif A[i][mid] < A[i][mid - 1]:
                    right = mid 
                else:
                    left = mid 
            if A[i - 1][mid] < A[i][mid] and A[i + 1][mid] < A[i][mid]:
                return [i, mid]
        return None 
        
        
        