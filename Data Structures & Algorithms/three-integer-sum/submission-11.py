class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            to_0 = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == to_0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] > to_0:
                    r -= 1
                else:
                    l += 1
        return output