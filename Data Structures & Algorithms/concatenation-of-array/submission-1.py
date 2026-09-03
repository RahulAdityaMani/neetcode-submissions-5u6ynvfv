class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * (2 * len(nums))
        for i in range(len(output)):
            output[i] = nums[i % len(nums)]
        return output