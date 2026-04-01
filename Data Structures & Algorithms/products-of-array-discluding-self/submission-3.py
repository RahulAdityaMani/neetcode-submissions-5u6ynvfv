class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        befores = [1] * len(nums)
        afters = [1] * len(nums)
        # [1 2 4 6]
        # befores: [1 1 2 8]
        # afters: [48 24 6 1]
        # [48 24 12 8]
        pre_prod = 1
        for i, num in enumerate(nums):
            befores[i] = pre_prod
            pre_prod *= num
        post_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            afters[i] = post_prod
            post_prod *= num
        prods = [1] * len(nums)
        for i in range(len(nums)):
            prods[i] = befores[i] * afters[i]
        return prods
            