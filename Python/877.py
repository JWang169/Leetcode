class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j]: the biggest number of stones you can get more than opponent picking piles in piles[i:j]
        dp = [[0] * n for _ in range(n)]
        
        # if there is only one pile: piles[i], what the first picker will get more than the seconde picker.
        for i in range(n):
            dp[i][i] = piles[i]
        
        # what will the first picker get more than the second picker if there are i-j piles to pick from
        for k in range(1, n):
            for i in range(0, n - k):
                j = i + k
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
                
        return dp[0][-1] > 0
        