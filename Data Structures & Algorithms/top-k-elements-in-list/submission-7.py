class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_to_freqs = Counter(nums)
        nums_per_freq = [[] for _ in range(len(nums))]
        for num, freq in nums_to_freqs.items():
            nums_per_freq[len(nums) - freq].append(num)
        top_k_freq = []
        freq_idx = 0
        while k > 0 and freq_idx < len(nums_per_freq):
            num_idx = 0
            while k > 0 and num_idx < len(nums_per_freq[freq_idx]):
                top_k_freq.append(nums_per_freq[freq_idx][num_idx])
                num_idx += 1
                k -= 1
            freq_idx += 1
        return top_k_freq