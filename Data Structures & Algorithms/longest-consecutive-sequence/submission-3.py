class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)

        sequence_starts = {}
        for num in nums_set:
            if num - 1 not in nums_set:
                sequence_starts[num] = []
        print(sequence_starts)

        max_seq = []
        for num in nums_set:
            if num in sequence_starts:
                curr_num = num + 1
                while curr_num in nums_set:
                    sequence_starts[num].append(curr_num)
                    curr_num += 1
                if len(sequence_starts[num]) + 1 > len(max_seq):
                    max_seq = sequence_starts[num]
        print(max_seq)
        return len(max_seq) + 1