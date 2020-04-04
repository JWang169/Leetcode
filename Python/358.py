class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.height = height
        self.width = width
        self.dirs = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        self.food = deque(food)
        self.scores = 0
        self.queue = deque([[0, 0]])
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        x, y = self.queue[0]
        dx, dy = self.dirs[direction]
        nx, ny = x + dx, y + dy
        
        if self.food:
            tx, ty = self.food[0][0], self.food[0][1]
        else:
            tx, ty = -1, -1
        last = self.queue.pop()
        if 0 <= ny < self.width and 0 <= nx < self.height and [nx, ny] not in self.queue:
            self.queue.appendleft([nx, ny])
            if nx == tx and ny == ty:
                self.scores += 1 
                self.food.popleft()
                self.queue.append(last)

            return self.scores
            
        else:
            return -1
            
            
        
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)