class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        freq_to_nums = [[] for i in range(len(nums))]
        for num in num_counts:
            freq_to_nums[num_counts[num] - 1].append(num)
        output = []
        for i in range(len(freq_to_nums) - 1, -1, -1):
            for num in freq_to_nums[i]:
                output.append(num)
                if len(output) == k:
                    return output

