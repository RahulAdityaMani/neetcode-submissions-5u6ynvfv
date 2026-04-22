class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        running = 1
        for num in nums:
            pre.append(running)
            running *= num
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            pre[i] *= running
            num = nums[i]
            running *= num
        return pre