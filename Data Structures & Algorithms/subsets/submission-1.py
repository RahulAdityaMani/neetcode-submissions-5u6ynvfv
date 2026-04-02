class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def _subsets(subset: List[int], i: int):
            if i == len(nums):
                output.append(subset.copy())
            else:
                _subsets(subset, i + 1)
                subset.append(nums[i])
                _subsets(subset, i + 1)
                subset.pop()
        _subsets(list(), 0)
        return output
            
            