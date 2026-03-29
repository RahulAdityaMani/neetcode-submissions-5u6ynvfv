class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min_buy_price = prices[0]
        for price in prices:
            curr_sell_price = price
            curr_profit = curr_sell_price - curr_min_buy_price
            max_profit = max(max_profit, curr_profit)
            curr_min_buy_price = min(curr_min_buy_price, price)
        return max_profit