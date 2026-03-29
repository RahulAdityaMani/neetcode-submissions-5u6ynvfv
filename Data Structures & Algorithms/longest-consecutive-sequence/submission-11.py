class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        boundaries = {}
        seen = set()
        for num in nums:
            if num not in seen:
                len_longest_seq_to_left = boundaries.get(num - 1, 0)
                len_longest_seq_to_right = boundaries.get(num + 1, 0)
                len_longest_seq_with_num = 1 + len_longest_seq_to_left + len_longest_seq_to_right
                seen.add(num)
                boundaries[num - len_longest_seq_to_left] = len_longest_seq_with_num
                boundaries[num + len_longest_seq_to_right] = len_longest_seq_with_num
                longest = max(longest, len_longest_seq_with_num)
        return longest