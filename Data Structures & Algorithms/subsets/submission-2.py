class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            for subset_i in range(len(output)):
                new_subset = output[subset_i][:]
                new_subset.append(num)
                output.append(new_subset)
        return output