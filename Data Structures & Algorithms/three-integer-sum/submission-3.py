class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = []
        for i in range(len(sorted_nums) - 2):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            i1 = i
            target = 0 - sorted_nums[i1]
            i2, i3 = i + 1, len(sorted_nums) - 1
            while i2 < i3:
                if sorted_nums[i2] + sorted_nums[i3] == target:
                    output.append([sorted_nums[i1], sorted_nums[i2], sorted_nums[i3]])
                    i2 += 1
                    i3 -= 1
                    while i2 < i3 and sorted_nums[i2] == sorted_nums[i2 - 1]:
                        i2 += 1
                    while i2 < i3 and sorted_nums[i3] == sorted_nums[i3 + 1]:
                        i3 -= 1
                elif sorted_nums[i2] + sorted_nums[i3] > target:
                    i3 -= 1
                else:
                    i2 += 1
        return output