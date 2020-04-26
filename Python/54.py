class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        result = []
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while up <= down or left <= right:
            # up
            if up <= down:
                for j in range(left, right + 1):
                    result.append(matrix[up][j])
                up += 1 
            if left <= right:
                for i in range(up, down + 1):
                    result.append(matrix[i][right])
                right -= 1 
            if up <= down:       
                for j in range(right, left - 1, -1):
                    result.append(matrix[down][j])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    result.append(matrix[i][left])   
                left += 1 

        return result
                    
            
            
            