class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        curr_prod = 1
        for num in nums:
            pre.append(curr_prod)
            curr_prod *= num
        post = [1]*len(nums)
        curr_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = curr_prod
            curr_prod *= nums[i]
        output = []
        print(pre, post)
        for i in range(len(pre)):
            output.append(pre[i] * post[i])
        return output