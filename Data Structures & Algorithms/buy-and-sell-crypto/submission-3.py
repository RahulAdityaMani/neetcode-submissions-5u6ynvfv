class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        curr_min = float("infinity")
        for price in prices:
            profits.append(price - curr_min)
            curr_min = min(price, curr_min)
        max_profit = max(profits)
        return max_profit if max_profit > 0 else 0