class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            for i in range(len(output)):
                subset = output[i].copy()
                subset.append(num)
                output.append(subset)
        return output