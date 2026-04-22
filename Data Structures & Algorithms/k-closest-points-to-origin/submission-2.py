class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points   
        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            points[i] = (x**2 + y**2, point)
        heapq.heapify(points)
        output = []
        while k > 0:
            output.append(heapq.heappop(points)[1])
            k -= 1
        return output