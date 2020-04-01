class Solution:
    def minimumDistance(self, word: str) -> int:
        # 3d的dp, 摸着良心说这道题你是人吗 
        # 是的 所以肯定可以不用3d就能做
        # 其实这道题和campus bike II 那道题的思路有一点像
        # dp[n][i][j] 代表打出第n个字母的时候，左手在i，右手在j，dist是多少 
        # self.dp = [[[-1] * 27 for _ in range(27)] for _ in range(n)]  
        
        self.seen = dict()
        return self.dfs(0, -1, -1, word)
        
        
    def dfs(self, i, left, right, word):
        if i == len(word):
            return 0
        if (i, left, right) in self.seen:
            return self.seen[(i, left, right)]
        
        c = ord(word[i]) - 65
        # use left fingure to type word[i], so left fingure move from word[i] to current left, right fingure stays
        moveLeft = self.dist(left, c) + self.dfs(i + 1, c, right, word) 
        # use right fingure to type word[i], so right fingure move from word[i] to current right, left fingure stays
        moveRight = self.dist(right, c)  + self.dfs(i + 1, left, c, word)
        self.seen[(i, left, right)] = min(moveLeft, moveRight)
        return self.seen[(i, left, right)]
               
        
    def dist(self, a, b): 
        if a == -1 or b == -1:
            return 0
        ax, ay = a // 6, a % 6
        bx, by = b // 6, b % 6
        return abs(ax - bx) + abs(ay - by)
        
        
    
        