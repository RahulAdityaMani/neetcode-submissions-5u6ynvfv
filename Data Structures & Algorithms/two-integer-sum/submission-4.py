class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            curr_num = nums[i]
            if target - curr_num in seen:
                return [seen[target - curr_num], i]
            seen[curr_num] = i
        return []