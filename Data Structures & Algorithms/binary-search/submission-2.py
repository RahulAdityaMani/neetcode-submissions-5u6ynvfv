class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m = 0, len(nums) - 1, len(nums) // 2
        while r - l + 1 > 2:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
                m = (r + l) // 2
            else:
                l = m
                m = (r + l) // 2
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1