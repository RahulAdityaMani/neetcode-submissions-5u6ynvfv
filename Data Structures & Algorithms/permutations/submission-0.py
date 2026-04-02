class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        perm = []
        picked = [False] * len(nums)
        def dfs():
            if len(perm) == len(nums):
                output.append(perm.copy())
                return
            for i in range(len(nums)):
                num = nums[i]
                num_picked = picked[i]
                if not num_picked:
                    perm.append(num)
                    picked[i] = True
                    dfs()
                    picked[i] = False
                    perm.pop()
        dfs()
        return output