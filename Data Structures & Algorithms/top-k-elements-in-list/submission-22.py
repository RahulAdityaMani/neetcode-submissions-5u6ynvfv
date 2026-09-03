class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_counts = Counter(nums)
        max_poss_freq = len(nums)
        nums_per_freq = [[] for _ in range(max_poss_freq)]
        for num, count in num_to_counts.items():
            nums_per_freq[count - 1].append(num)
        output = []
        i = max_poss_freq - 1
        while k > 0 and i >= 0:
            curr_freq_nums = nums_per_freq[i]
            for num in curr_freq_nums:
                output.append(num)
                k -= 1
                if k == 0:
                    break
            i -= 1
        return output
