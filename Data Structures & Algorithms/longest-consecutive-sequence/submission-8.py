class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        boundaries = {}
        nums_set = set(nums)
        for num in nums_set:
            len_longest_seq_to_left = boundaries.get(num - 1, 0)
            len_longest_seq_to_right = boundaries.get(num + 1, 0)
            len_seq_with_num = 1 + len_longest_seq_to_left + len_longest_seq_to_right
            boundaries[num - len_longest_seq_to_left] = len_seq_with_num
            boundaries[num + len_longest_seq_to_right] = len_seq_with_num
            longest = max(longest, len_seq_with_num)
        return longest