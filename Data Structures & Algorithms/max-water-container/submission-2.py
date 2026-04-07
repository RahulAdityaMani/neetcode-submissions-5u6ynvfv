class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            height_l = heights[l]
            height_r = heights[r]
            width = r - l
            area = min(height_l, height_r) * width
            max_area = max(max_area, area)
            if height_l < height_r:
                l += 1
            else:
                r -= 1
        return max_area