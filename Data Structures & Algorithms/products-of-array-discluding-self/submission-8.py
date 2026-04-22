class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pes = []
        running = 1
        for num in nums:
            pes.append(running)
            running *= num
        running = 1
        for i in range(len(nums) - 1, -1, -1):
            pes[i] *= running
            num = nums[i]
            running *= num
        return pes