class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] <= prices[buy]:
                buy = i
                continue
            result += prices[i] - prices[buy]
            buy = i
        return result