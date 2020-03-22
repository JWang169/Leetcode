class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        result = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.search(i, j, board)
                if board[i][j] == 0 and count == 3:
                    result[i][j] = 1
                if board[i][j] == 1 and 2 <= count <= 3:
                    result[i][j] = 1
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = result[i][j]
    
    def search(self, x, y, board):
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        count = 0
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == 1:
                    count += 1 
        return count 