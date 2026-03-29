class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        curr_prod = 1
        for num in nums:
            output.append(curr_prod)
            curr_prod *= num
        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= curr_prod
            curr_prod *= nums[i]
        return output