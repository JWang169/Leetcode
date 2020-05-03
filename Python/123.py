class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            curMin = prices[0]
            for i in range(1, n):
                # if we buy on day j, sell on day i, the profit is prices[i] - prices[j] + dp[k - 1][j]
                curMin = min(curMin, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - curMin)
        return dp[2][n - 1]
        
        
#         if len(prices) < 2:
#             return 0
#         n = len(prices) 
#         # dp[k, i]: profit on k_th transactions, i_th day 
#         dp = [[0] * n for _ in range(3)]
#         for k in range(1, 3):
#             for i in range(1, n): # find the maximum profit when sell on day i 
#                 maxProfit = max(0, prices[i] - prices[0])
#                 for j in range(1, i): # buy on day j and sell on day i
#                     maxProfit = max(maxProfit, dp[k - 1][j - 1] + prices[i] - prices[j])
#                 dp[k][i] = max(maxProfit, dp[k][i - 1])
        
#         print(dp)
#         return dp[2][n - 1]
        
        
        
        


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy1, sell1 = -sys.maxsize, 0
#         buy2, sell2 = -sys.maxsize, 0
#         for price in prices:
#             if buy1 < -price:
#                 buy1 = -price
#             if sell1 < buy1 + price:
#                 sell1 = buy1 + price
#             if buy2 < sell1 - price:
#                 buy2 = sell1 - price
#             if sell2 < buy2 + price:
#                 sell2 = buy2 + price
        
#         return sell2
        


