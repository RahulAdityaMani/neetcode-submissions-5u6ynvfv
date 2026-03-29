class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR, trapped = 0, 0, 0
        while l < r:
            left, right = height[l], height[r]
            if left < right:
                if left > maxL:
                    maxL = left
                else:
                    trapped += maxL - left
                l += 1
            else:
                if right > maxR:
                    maxR = right
                else:
                    trapped += maxR - right
                r -= 1
        return trapped