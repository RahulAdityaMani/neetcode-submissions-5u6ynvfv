class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        output = set()
        for i in range(len(sorted_nums) - 2):
            i1 = i
            target = 0 - sorted_nums[i1]
            for j in range(i + 1, len(sorted_nums) - 1):
                i2 = j
                i3 = len(sorted_nums) - 1
                found_triplet = False
                while i2 < i3 and not found_triplet:
                    if sorted_nums[i2] + sorted_nums[i3] == target:
                        found_triplet = True
                    elif sorted_nums[i2] + sorted_nums[i3] > target:
                        i3 -= 1
                    else:
                        i2 += 1
                if found_triplet:
                    output.add(tuple([sorted_nums[i1], sorted_nums[i2], sorted_nums[i3]]))
        return list(output)