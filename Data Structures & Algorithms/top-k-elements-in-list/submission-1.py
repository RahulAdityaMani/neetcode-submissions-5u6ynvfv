class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = sorted(Counter(nums).items(), key = lambda kv: kv[1])
        output = []
        for i in range(len(a)-1, len(a) - k - 1, -1):
            output.append(a[i][0])
        return output
