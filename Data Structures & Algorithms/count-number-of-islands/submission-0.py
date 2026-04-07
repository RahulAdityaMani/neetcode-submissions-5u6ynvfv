class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited = set()
        def helper(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))
            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    helper(i, j)
                    num_islands += 1
        return num_islands