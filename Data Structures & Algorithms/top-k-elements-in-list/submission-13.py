class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_to_nums = defaultdict(list)
        for num, freq in counts.items():
            freq_to_nums[freq].append(num)
        max_poss_freq = len(nums)
        output = []
        for freq in range(max_poss_freq, -1, -1):
            if freq in freq_to_nums:
                for num in freq_to_nums[freq]:
                    output.append(num)
                    k -= 1
                    if k == 0:
                        return output
        