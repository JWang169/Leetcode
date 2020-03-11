class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        prev = [0] * len(grid[0])
        for i in range(len(grid)):
            cur = []
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    cur.append(grid[i][j])
                    continue
                if i == 0:
                    cur.append(cur[j - 1] + grid[i][j])
                    continue
                if j == 0:
                    cur.append(prev[j] + grid[i][j])
                    continue
                cur.append(min(prev[j], cur[j - 1]) + grid[i][j])
            prev = cur
        return prev[-1]
                    