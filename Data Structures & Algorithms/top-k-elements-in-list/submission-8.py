class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_to_nums = [[] for _ in range(len(nums))]
        for num, freq in counts.items():
            freq_to_nums[len(nums) - freq].append(num)
        topK = []
        for freq_lst in freq_to_nums:
            for num in freq_lst:
                topK.append(num)
                k -= 1
                if k == 0:
                    return topK