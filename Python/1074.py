class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # presum matrix
        for i in range(m):
            for j in range(n - 1):
                matrix[i][j + 1] += matrix[i][j]
        
        res = 0
        for i in range(n):
            for j in range(i, n):
                cols = collections.defaultdict(int)
                cur, cols[0] = 0, 1

                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    res += cols[cur - target]
                    cols[cur] += 1 
        return res
        
        