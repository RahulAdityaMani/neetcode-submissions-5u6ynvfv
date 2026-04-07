class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        pq = []
        print(counts)
        for num, freq in counts.items():
            heapq.heappush(pq, (-freq, num))
        output = []
        while k > 0:
            output.append(heapq.heappop(pq)[1])
            k -= 1
        return output