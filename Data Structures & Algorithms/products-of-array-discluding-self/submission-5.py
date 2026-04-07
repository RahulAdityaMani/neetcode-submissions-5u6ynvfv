class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprods = [1] * len(nums)
        for i in range(1, len(nums)):
            preprods[i] = nums[i-1] * preprods[i - 1]
        postprods = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postprods[i] = nums[i + 1] * postprods[i + 1]
        output = [1] * len(nums)
        for i in range(len(preprods)):
            output[i] = preprods[i] * postprods[i]
        return output