class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 100
        for curr_price in prices:
            curr_profit = curr_price - min_buy
            max_profit = max(max_profit, curr_profit)
            min_buy = min(min_buy, curr_price)
        return max_profit
        