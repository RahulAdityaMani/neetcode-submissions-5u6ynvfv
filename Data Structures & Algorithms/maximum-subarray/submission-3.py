class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        l, r = 0, 1
        curr_sum = nums[0]
        max_sum = nums[0]
        while r < len(nums):
            if curr_sum < 0:
                curr_sum = 0
                l = r
            curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)
            r += 1
        return max_sum