class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def rob_helper (i: int) -> int:
            if i in cache:
                return cache[i]
            if i >= len(nums):
                cache[i] = 0
                return cache[i]
            if i == len(nums) - 1:
                cache[i] = nums[i]
                return cache[i]
            if i == len(nums) - 2:
                cache[i] = max(nums[i], nums[i + 1])
                return cache[i]
            cache[i] = max(nums[i] + rob_helper(i + 2), rob_helper(i + 1))
            return cache[i]
        return rob_helper(0)