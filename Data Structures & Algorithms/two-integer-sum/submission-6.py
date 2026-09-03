class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            to_go = target - num
            if to_go in seen:
                return [seen[to_go], i]
            seen[num] = i