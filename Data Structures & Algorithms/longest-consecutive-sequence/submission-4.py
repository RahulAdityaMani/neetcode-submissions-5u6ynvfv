class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)

        sequence_starts = set()
        for num in nums_set:
            if num - 1 not in nums_set:
                sequence_starts.add(num)

        len_max_seq = 0
        for num in nums_set:
            if num in sequence_starts:
                len_curr_seq = 1
                curr_num = num + 1
                while curr_num in nums_set:
                    curr_num += 1
                    len_curr_seq += 1
                len_max_seq = max(len_max_seq, len_curr_seq)
        
        return len_max_seq
        