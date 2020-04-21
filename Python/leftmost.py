# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        
        n, m = binaryMatrix.dimensions()
        result = m
        
        for i in range(n):
            left, right = 0, m - 1
            while left + 1 < right:
                mid = (left + right) // 2 
                num = binaryMatrix.get(i, mid)
                if num == 1:
                    right = mid 
                else:
                    left = mid + 1
            if binaryMatrix.get(i, left) == 1:
                result = min(left, result)
            elif binaryMatrix.get(i, right) == 1:
                result = min(right, result)
        
        return result if result < m else -1
                    
                    
                    
                
                
                
                
                
                
                
                
        
        