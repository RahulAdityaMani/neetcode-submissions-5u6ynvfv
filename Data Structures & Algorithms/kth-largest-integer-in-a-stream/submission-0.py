import heapq

class KthLargest:

    

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for num in nums:
            heapq.heappush(self.pq, (num, num))
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq, (val, val))
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0][0]

