class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        poss_starts = []
        for num in nums:
            if num - 1 not in seen:
                poss_starts.append(num)
        max_seq_len = 0
        for poss_start in poss_starts:
            curr_seq_len = 1
            curr_num = poss_start + 1
            while curr_num in seen:
                curr_seq_len += 1
                curr_num += 1
            max_seq_len = max(max_seq_len, curr_seq_len)
        return max_seq_len

