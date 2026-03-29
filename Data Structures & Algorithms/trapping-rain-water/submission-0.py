class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts, max_rights = [height[0]]*len(height), [height[len(height) - 1]]*len(height)
        for i in range(1, len(height)):
            if height[i] > max_lefts[i - 1]:
                max_lefts[i] = height[i]
            else:
                max_lefts[i] = max_lefts[i - 1]

        for i in range(len(height) - 2, -1, -1):
            if height[i] > max_rights[i + 1]:
                max_rights[i] = height[i]
            else:
                max_rights[i] = max_rights[i + 1]

        trapped = 0
        for i in range(len(height)):
            trapped += (min(max_lefts[i], max_rights[i]) - height[i])
        return trapped
        