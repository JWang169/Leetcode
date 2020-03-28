class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0
        m, n = len(A), len(A[0])
        visited = [[False] * n for _ in range(m)]
        
        mi = A[0][0]
        heap = [(-mi, 0, 0)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        while heap:
            curMin, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return -curMin
            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    newMin = min(-curMin, A[nx][ny])
                    heapq.heappush(heap, (-newMin, nx, ny))
        return -1
        
        