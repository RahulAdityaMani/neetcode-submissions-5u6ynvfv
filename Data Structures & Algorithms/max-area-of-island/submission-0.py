class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def islandArea(r, c):
            if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + islandArea(r + 1, c) + islandArea(r - 1, c) + islandArea(r, c + 1) + islandArea(r, c - 1)
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = islandArea(i, j)
                    max_area = max(max_area, curr_area)
        return max_area