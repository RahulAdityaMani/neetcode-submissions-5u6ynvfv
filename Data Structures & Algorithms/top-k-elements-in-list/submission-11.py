class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_to_nums = [[] for _ in range (len(nums) + 1)]
        for num, count in counts.items():
            freq_to_nums[count].append(num)
        output = []
        for i in range(len(freq_to_nums) - 1, -1, -1):
            curr_freq_nums = freq_to_nums[i]
            for num in curr_freq_nums:
                if k == 0:
                    return output
                output.append(num)
                k -= 1
        return output