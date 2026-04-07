class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(i: int):
            if i in cache:
                return cache[i]
            if i == n:
                cache[i] = 1
                return 1
            if i == n - 1:
                cache[i] = 1
                return 1
            if i == n - 2:
                cache[i] = 2
                return 2
            cache[i] = helper(i + 1) + helper(i + 2)
            return cache[i]
        return helper(0)
            
            