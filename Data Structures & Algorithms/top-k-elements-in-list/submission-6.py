class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = Counter(nums)
        sorted_freqs = [[] for _ in range(len(nums))]
        # for num, freq in num_to_freq.items():
        #     sorted_freqs[len(nums) - freq].append(num)
        # output = []
        # for freq_lst in sorted_freqs:
        #     for num in freq_lst:
        #         output.append(num)
        #         k -= 1
        #         if k == 0:
        #             return output
        for num, freq in num_to_freq.items():
            sorted_freqs[freq - 1].append(num)
        output = []
        for i in range(len(sorted_freqs) - 1, -1, -1):
            freq_lst = sorted_freqs[i]
            for num in freq_lst:
                output.append(num)
                k -= 1
                if k == 0:
                    return output
