class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = 0
        max_profit = 0
        for sell in range(1, len(prices)):
            if prices[sell] <= prices[buy]:
                buy = sell
            else:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)
        return max_profit