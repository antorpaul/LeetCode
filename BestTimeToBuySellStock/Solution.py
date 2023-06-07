class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy: int = 0
        sell: int = 1
        maxProfit: int = 0

        while sell < len(prices):
            currentProfit: int = prices[sell] - prices[buy]
            maxProfit = max(currentProfit, maxProfit)

            if prices[sell] < prices[buy]:
                buy = sell
            
            sell += 1
            
        return maxProfit