class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            num_can_jump = nums[i]
            if num_can_jump + i >= goal:
                goal = i
        return goal == 0