class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = float('infinity')
        cache = {}
        def helper(i: int):
            nonlocal min_cost
            if i in cache:
                return cache[i]
            if i == len(cost):
                cache[i] = 0
                return cache[i]
            if i == len(cost) - 1:
                cache[i] = cost[i]
                return cache[i]
            cache[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            min_cost = min(min_cost, cache[i])
            return cache[i]
        return min(helper(0), helper(1))