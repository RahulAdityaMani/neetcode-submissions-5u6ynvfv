class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_len = 1
        for num in nums:
            if num - 1 not in nums_set: # sequence start
                curr_len = 1
                curr_num = num + 1
                while curr_num in nums_set:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
        return max_len