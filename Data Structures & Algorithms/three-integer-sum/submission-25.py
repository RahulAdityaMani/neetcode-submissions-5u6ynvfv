class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum > target:
                    k -= 1
                    while j < k and k < len(nums) - 1 and nums[k] == nums[k + 1]:
                        k -= 1
                elif curr_sum < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and k < len(nums) - 1 and nums[k] == nums[k + 1]:
                        k -= 1
        return output