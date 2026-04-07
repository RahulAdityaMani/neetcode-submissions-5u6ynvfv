class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            target = 0 - a
            j, k = i + 1, len(nums) - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if b + c > target:
                    k -= 1
                    while j < k and nums[k] == c:
                        k -= 1
                elif b + c < target:
                    j += 1
                    while j < k and nums[j] == b:
                        j += 1
                else:
                    output.append([a, b, c])
                    k -= 1
                    while j < k and nums[k] == c:
                        k -= 1
                    j += 1
                    while j < k and nums[j] == b:
                        j += 1
        return output

