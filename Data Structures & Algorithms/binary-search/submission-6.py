class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(l, r):
            if l > r:
                return -1
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return _search(l, m - 1)
            else:
                return _search(m + 1, r)
        return _search(0, len(nums) - 1)