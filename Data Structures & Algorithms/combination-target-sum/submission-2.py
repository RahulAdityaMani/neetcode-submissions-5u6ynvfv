class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combo = []
        def helper(i, curr_total):
            if curr_total == target:
                output.append(combo[:])
                return
            if curr_total > target:
                return
            if i == len(nums):
                return
            combo.append(nums[i])
            helper(i, curr_total + nums[i])
            combo.pop()
            helper(i + 1, curr_total)
        helper(0, 0)
        return output