class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def helper(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or grid[r][c] == 2:
                return 0
            grid[r][c] = 2
            num_edges = 0
            if r == 0 or grid[r - 1][c] == 0:
                num_edges += 1
            if c == 0 or grid[r][c - 1] == 0:
                num_edges += 1
            if r == len(grid) - 1 or grid[r + 1][c] == 0:
                num_edges += 1
            if c == len(grid[0]) - 1 or grid[r][c + 1] == 0:
                num_edges += 1
            num_edges = num_edges + helper(r + 1, c) + helper(r - 1, c) + helper(r, c + 1) + helper(r, c - 1)
            return num_edges
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return helper(i, j)
        return 0