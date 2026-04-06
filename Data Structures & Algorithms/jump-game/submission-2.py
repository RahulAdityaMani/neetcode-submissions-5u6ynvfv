class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [False] * len(nums)
        cache[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            num_can_jump = nums[i]
            for j in range(1, num_can_jump + 1):
                if i + j >= len(nums) - 1 or cache[i + j]:
                    cache[i] = True
                    break
        return cache[0]