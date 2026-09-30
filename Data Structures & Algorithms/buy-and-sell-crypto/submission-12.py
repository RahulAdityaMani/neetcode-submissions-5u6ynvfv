class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        max_p = 0
        while s < len(prices):
            if prices[s] < prices[b]:
                b = s
            else:
                profit = prices[s] - prices[b]
                max_p = max(max_p, profit)
            s += 1
        return max_p
