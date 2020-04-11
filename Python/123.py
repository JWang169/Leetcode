class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1 = -sys.maxsize, 0
        buy2, sell2 = -sys.maxsize, 0
        for price in prices:
            if buy1 < -price:
                buy1 = -price
            if sell1 < buy1 + price:
                sell1 = buy1 + price
            if buy2 < sell1 - price:
                buy2 = sell1 - price
            if sell2 < buy2 + price:
                sell2 = buy2 + price
        
        return sell2
        


