



O(n^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i]: max profit on ith day 
        # dp[i] = max(dp[i - 1], prices[i] - prices[j] + dp[j - 2])
        
        if len(prices) < 2:
            return 0
        
        n = len(prices)
        dp = [0] * n
        
        for i in range(1, n):
            if i == 1:
                dp[i] = max(0, prices[1] - prices[0])
            else:
                dp[i] = dp[i - 1] # cool down
                for j in range(i):
                    # prev 是 day j 之前的最大收益
                    prev = dp[j - 2] if j > 1 else 0
                    dp[i] = max(dp[i], prev + prices[i] - prices[j])
                
        return dp[n - 1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i]: max profit on ith day 
        # dp[i] = max(dp[i - 1], prices[i] - prices[j] + dp[j - 2])
        
        if len(prices) < 2:
            return 0
        
        n = len(prices)
        dp = [0] * (n + 1)
        
        curMin = prices[0]
        for i in range(1, n):
            curMin = min(curMin, prices[i] - dp[i - 1])
            dp[i + 1] = max(dp[i], prices[i] - curMin)
        
        return dp[n]
        