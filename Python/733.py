class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        if target == newColor:
            return image
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        queue = deque([[sr, sc]])
        while queue:
            x, y = queue.popleft()
            image[x][y] = newColor
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == target:
                    queue.append([nx, ny])
        return image
        