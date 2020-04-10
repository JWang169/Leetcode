class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat or not mat[0]:
            return -1
        m, n = len(mat), len(mat[0])
        d = min(m, n)
        # f[i][j]: prefix sum of row[: i] and col[:j]??
        
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j] + f[i][j - 1] - f[i - 1][j - 1] + mat[i - 1][j - 1]
        print(f)
        # the side-length
        count = 0
        for r in range(1, d + 1):
            found = False 
            for i in range(r, m + 1):
                if found:
                    break
                for j in range(r, n + 1):
                    if f[i][j] - f[i - r][j] - f[i][j - r] + f[i - r][j - r] <= threshold:
                        count = r
                        found = True
                        break
            if not found:
                break
        return count 
                    
                    
        
        
        