class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist_sq = point[0] ** 2 + point[1] ** 2
            heapq.heappush(max_heap, (-dist_sq, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [x[1] for x in max_heap]