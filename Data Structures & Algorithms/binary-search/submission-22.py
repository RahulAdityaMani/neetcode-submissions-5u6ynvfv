class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = -1, len(nums) - 1
        while l < r:
            m = l + ((r - l + 1) // 2)
            if nums[m] < target:
                l = m
            elif nums[m] >= target:
                r = m - 1
        return r + 1 if r < len(nums) - 1 and nums[r + 1] == target else - 1