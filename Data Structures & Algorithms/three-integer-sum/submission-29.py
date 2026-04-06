class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            target = 0 - a
            j = i + 1
            k = len(nums) - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if b + c > target:
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                elif b + c < target:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                else:
                    triplets.append([a, b, c])
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
        return triplets
                
