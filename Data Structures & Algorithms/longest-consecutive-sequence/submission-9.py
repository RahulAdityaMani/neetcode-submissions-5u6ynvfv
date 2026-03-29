class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        boundaries = defaultdict(int)
        for num in nums:
            if boundaries[num] == 0:
                len_longest_seq_to_left = boundaries.get(num - 1, 0)
                len_longest_seq_to_right = boundaries.get(num + 1, 0)
                len_longest_seq_with_num = 1 + len_longest_seq_to_left + len_longest_seq_to_right
                boundaries[num] = len_longest_seq_with_num
                boundaries[num - len_longest_seq_to_left] = len_longest_seq_with_num
                boundaries[num + len_longest_seq_to_right] = len_longest_seq_with_num
                longest = max(longest, len_longest_seq_with_num)
                print(boundaries)
        return longest