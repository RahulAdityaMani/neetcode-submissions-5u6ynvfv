class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def helper(i: int):
            if i in cache:
                return cache[i]
            if i >= len(cost):
                cache[i] = 0
                return 0
            cache[i] = min(cost[i] + helper(i + 2), cost[i] + helper(i + 1))
            return cache[i]
        print(cache)
        return min(helper(0), helper(1))