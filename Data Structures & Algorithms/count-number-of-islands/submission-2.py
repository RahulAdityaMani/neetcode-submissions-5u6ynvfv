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
                    queue = deque([island_start])
                    visited.add(island_start)
                    while queue:
                        land_i, land_j = queue.popleft()
                        offsets = [(-1, 0), (0, 1), (0, -1), (1, 0)]
                        for offset_i, offset_j in offsets:
                            if land_i + offset_i < 0 or land_i + offset_i >= len(grid) or land_j + offset_j < 0 or land_j + offset_j >= len(grid[0]) or (land_i + offset_i, land_j + offset_j) in visited:
                                continue
                            if grid[land_i + offset_i][land_j + offset_j] == "1":
                                visited.add((land_i + offset_i, land_j + offset_j))
                                queue.append((land_i + offset_i, land_j + offset_j))
                    num_islands += 1
        return num_islands

                
