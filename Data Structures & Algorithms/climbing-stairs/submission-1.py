class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def helper(num_steps: int):
            if num_steps in cache:
                return cache[num_steps]
            if num_steps <= 1:
                cache[num_steps] = 1
                return cache[num_steps]
            cache[num_steps] = helper(num_steps - 1) + helper(num_steps - 2)
            return cache[num_steps]
        return helper(n)