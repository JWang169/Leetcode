class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # 1. the 2D case as two independent 1D problems
        # 2. the median must be the optimal meeting point.
        xs, ys = [], []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    xs.append(i)
                    ys.append(j)
        xs.sort()
        ys.sort()
        num = len(xs)
        mx, my = xs[num // 2], ys[num // 2]
        result = 0
        for i in range(num):
            result += abs(xs[i] - mx) + abs(ys[i] - my)
        return result
                
        
        
        
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        people = [] # coords of 1s  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    people.append([i, j])
        
        result = sys.maxsize
        for i in range(m):
            for j in range(n):
                dist = 0
                for x, y in people:
                    dist += abs(i - x) + abs(j - y)
                result = min(result, dist)
        return result 
        """

        
        
        
        