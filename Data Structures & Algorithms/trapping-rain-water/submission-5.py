class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [height[0]] * len(height)
        for i in range(1, len(height)):
            if height[i] > maxL[i - 1]:
                maxL[i] = height[i]
            else:
                maxL[i] = maxL[i - 1]
        maxR = [height[len(height) - 1]] * len(height)
        for i in range (len(height) - 2, -1, -1):
            if height[i] > maxR[i + 1]:
                maxR[i] = height[i]
            else:
                maxR[i] = maxR[i + 1]
        trapped = 0
        for i in range(len(height)):
            curr_height = height[i]
            max_possible = min(maxL[i], maxR[i])
            curr_trapped = max_possible - curr_height
            trapped += curr_trapped
        return trapped