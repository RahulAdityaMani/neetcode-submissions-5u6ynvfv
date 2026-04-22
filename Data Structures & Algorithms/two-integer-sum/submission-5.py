class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            togo = target - num
            if togo in seen:
                return [seen[togo], i]
            seen[num] = i