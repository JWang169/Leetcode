class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]
        
        for i in range(2, numRows):
            cur = [1]
            prev = result[i - 1]
            for j in range(1, i):
                cur.append(prev[j - 1] + prev[j])
            cur.append(1)
            result.append(cur)
        return result
        
        
        