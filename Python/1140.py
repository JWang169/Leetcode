class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.seen = {}
        
        res = self.dfs(1, piles)
        return res
        
    def dfs(self, m, piles):
        n = len(piles)
        if (m, n) in self.seen:
            return self.seen[(m, n)]
        
        if not piles:
            return 0
        
        if 2 * m >= n:
            self.seen[(m, n)] = sum(piles)
            return self.seen[(m, n)]
        
        mi = sys.maxsize
        total = sum(piles)
        for i in range(1, 2 * m + 1):
            nxt = self.dfs(max(i, m), piles[i:])
            mi = min(mi, nxt)
        self.seen[(m, n)] = total - mi
        return self.seen[(m, n)]