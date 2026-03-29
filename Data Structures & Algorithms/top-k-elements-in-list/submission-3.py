class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        digit_counts = Counter(nums)
        freq_to_digits = [[] for i in range(len(nums))]
        for digit in digit_counts:
            freq_to_digits[digit_counts[digit] - 1].append(digit)
        output = []
        # for i in range(len(freq_to_digits) - 1, -1, -1):
        #     for digit in freq_to_digits[i]:
        #         output.append(digit)
        #         if len(output) == k:
        #             return output
        curr_freq_idx = len(freq_to_digits) - 1
        while len(output) < k and curr_freq_idx >= 0:
            curr_freq_dig_lst = freq_to_digits[curr_freq_idx]
            curr_dig_idx = 0
            while len(output) < k and curr_dig_idx < len(curr_freq_dig_lst):
                output.append(curr_freq_dig_lst[curr_dig_idx])
                curr_dig_idx += 1
            curr_freq_idx -= 1
        return output

