class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr_min_buy = float("infinity")
        for selling_price in prices:
            max_profit = max(max_profit, selling_price - curr_min_buy)
            curr_min_buy = min(selling_price, curr_min_buy)
        return max_profit