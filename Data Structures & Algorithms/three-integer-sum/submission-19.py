class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i == 0 or nums[i-1] != nums[i]:
                j, k = i + 1, len(nums) - 1
                to_zero = 0 - nums[i]
                while j < k:
                    if nums[j] + nums[k] == to_zero:
                        triplets.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
                    elif nums[j] + nums[k] > to_zero:
                        k -= 1
                    else:
                        j += 1
        return triplets