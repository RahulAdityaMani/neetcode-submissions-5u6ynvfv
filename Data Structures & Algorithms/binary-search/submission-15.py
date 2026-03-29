class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def _search(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = left + ((right - left) // 2)
            if nums[mid] > target:
                return _search(left, mid - 1)
            elif nums[mid] < target:
                return _search(mid + 1, right)
            else:
                return mid
        return _search(0, len(nums) - 1)
