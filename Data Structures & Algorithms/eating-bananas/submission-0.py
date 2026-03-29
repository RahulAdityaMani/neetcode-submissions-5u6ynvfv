class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = float('-infinity')
        for pile in piles:
            max_k = max(max_k, pile)
        left = 1
        right = max_k + 1
        while left < right:
            mid = left + ((right - left) // 2)
            t = 0
            for pile in piles:
                t += math.ceil(pile / mid)
            if t <= h:
                right = mid
            else:
                left = mid + 1
        if left < max_k + 1:
            return left
        return -1
