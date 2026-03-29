class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        boundaries = defaultdict(int)
        seen = set()
        for num in nums:
            if num not in seen:
                len_longest_seq_to_left = boundaries[num - 1]
                len_longest_seq_to_right = boundaries[num + 1]
                len_seq_with_num = 1 + len_longest_seq_to_left + len_longest_seq_to_right
                seen.add(num)
                boundaries[num - len_longest_seq_to_left] = len_seq_with_num
                boundaries[num + len_longest_seq_to_right] = len_seq_with_num
                longest = max(longest, len_seq_with_num)
        return longest