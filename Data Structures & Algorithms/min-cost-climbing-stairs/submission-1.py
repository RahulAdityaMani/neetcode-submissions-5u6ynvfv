class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def helper(i: int):
            if i in cache:
                return cache[i]
            if i >= len(cost):
                cache[i] = 0
                return 0
            if i == len(cost) - 1:
                cache[i] = cost[i]
                return cache[i]
            if i == len(cost) - 2:
                cache[i] = min(cost[i], cost[i] + helper(i + 1))
                return cache[i]
            cache[i] = min(cost[i] + helper(i + 2), cost[i] + helper(i + 1))
            return cache[i]
        print(cache)
        return min(helper(0), helper(1))