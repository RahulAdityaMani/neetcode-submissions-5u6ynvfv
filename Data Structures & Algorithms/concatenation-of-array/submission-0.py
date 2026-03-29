class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans_len = 2 * nums_len
        ans = [0] * ans_len
        for i in range(ans_len):
            ans[i] = nums[i % nums_len]
        return ans