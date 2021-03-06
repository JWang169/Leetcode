class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#           DP
        if not prices:
            return 0
        buy, sell = -prices[0], 0
        for price in prices[1:]:
            buy = max(buy, -price)
            sell = max(sell, price + buy)
        return sell
        
#           GREEDY
#         if not prices:
#             return 0
#         result = 0
#         cur = prices[0]
#         for i in range(1, len(prices)):
#             result = max(prices[i] - cur, result)
#             if prices[i] < cur:
#                 cur = prices[i]
            
#         return result