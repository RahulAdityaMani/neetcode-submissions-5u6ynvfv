class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        most_freq = sorted(num_count.items(), key=lambda item: item[1], reverse = True)
        print(most_freq)
        output = []
        for key in most_freq:
            output.append(key[0])
            k -= 1
            if k == 0:
                return output