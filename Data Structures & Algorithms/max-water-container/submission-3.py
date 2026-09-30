class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_a = 0
        while l < r:
            max_a = max(max_a, (r - l) * min(heights[r], heights[l]))
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_a