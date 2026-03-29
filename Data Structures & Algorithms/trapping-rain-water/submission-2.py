class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxL, maxR, trapped = 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > maxL:
                    maxL = height[left]
                else:
                    trapped += maxL - height[left]
                left += 1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    trapped += maxR - height[right]
                right -= 1
        return trapped