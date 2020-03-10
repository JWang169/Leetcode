class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        row = [0] * len(matrix[0])
        row.append(-1)
        result = 0
        for i in range(len(matrix)):  # row: top to bottom
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    row[j] = 0
                else:
                    row[j] += 1 
            area = self.helper(row)
            result = max(area, result)
            
        return result 
    
    def helper(self, row):
        ma = 0
        stack = []     
        for i, num in enumerate(row):
            while len(stack) > 0 and row[stack[-1]] >= num:
                h = row[stack.pop()]
                left = stack[-1] + 1 if len(stack) > 0 else 0
                right = i - 1
                area = h * (right - left + 1)
                ma = max(area, ma)
            stack.append(i) 
        return ma 
        