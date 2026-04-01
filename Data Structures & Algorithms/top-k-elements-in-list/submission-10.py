class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq_to_nums = [[] for _ in range(len(nums))]
        print(counts)
        print(freq_to_nums)
        #  6   5   4   3   2   1
        # [[], [], [], [], [], []]
        # 6 - 6
        # 5 - 6 * -1
        # 4 - 6 * -1 
        for num in counts:
            key = (counts[num] - len(nums)) * -1
            freq_to_nums[key].append(num)
        curr_k = k
        output = []
        for freq_nums in freq_to_nums:
            for num in freq_nums:
                if curr_k == 0:
                    return output
                output.append(num)
                curr_k -= 1
        return output