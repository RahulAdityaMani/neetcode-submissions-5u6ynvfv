class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, maxA = 0, len(heights) - 1, 0
        while l < r:
            left, right = heights[l], heights[r]
            width = r - l
            height = min(left, right)
            area = width * height
            maxA = max(maxA, area)
            if left < right:
                l += 1
            else:
                r -= 1
        return maxA