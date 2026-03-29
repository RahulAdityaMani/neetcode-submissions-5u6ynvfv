class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = Counter(nums)
        sorted_freqs = [[] for _ in range(len(nums))]
        for num, freq in num_to_freq.items():
            sorted_freqs[len(nums) - freq].append(num)
        output = []
        print(sorted_freqs)
        for freq_lst in sorted_freqs:
            for num in freq_lst:
                output.append(num)
                k -= 1
                if k == 0:
                    return output
