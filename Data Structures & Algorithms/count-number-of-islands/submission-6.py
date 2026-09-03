class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        for grid_i in range(len(grid)):
            for grid_j in range(len(grid[grid_i])):
                if grid[grid_i][grid_j] == "1":
                    island_start = (grid_i, grid_j)
                    if island_start in visited:
                        continue
                    stack = [island_start]
                    visited.add(island_start)
                    while stack:
                        land_i, land_j = stack.pop()
                        # if (land_i, land_j) in visited:
                        #     continue
                        # visited.add((land_i, land_j))
                        offsets = [(-1, 0), (0, 1), (0, -1), (1, 0)]
                        for offset_i, offset_j in offsets:
                            r, c = land_i + offset_i, land_j + offset_j
                            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited:
                                continue
                            if grid[r][c] == "1":
                                visited.add((r, c))
                                stack.append((r, c))
                    num_islands += 1
        return num_islands

                
