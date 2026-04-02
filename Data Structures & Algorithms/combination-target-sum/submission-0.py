class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        combo = []
        def dfs(i: int, curr_sum: int):
            if i == len(nums):
                return
            if curr_sum > target:
                return
            if curr_sum == target:
                output.append(combo.copy())
                return
            dfs(i + 1, curr_sum)
            combo.append(nums[i])
            dfs(i, curr_sum + nums[i])
            combo.pop()
        dfs(0, 0)
        return output
