class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return 
        INF = 2 ** 31 - 1 
        count = 0 
        queue = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
                elif rooms[i][j] == INF:
                    count += 1 

        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if rooms[nx][ny] > rooms[x][y] + 1:
                        rooms[nx][ny] = rooms[x][y] + 1
                        queue.append((nx, ny))
                        count -= 1 

        
            
        
        
        