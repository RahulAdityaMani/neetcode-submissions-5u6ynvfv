class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = deque([(i, j)])
                    grid[i][j] = 2
                    num_edges = 0
                    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    while queue:
                        r, c = queue.popleft()
                        for nr, nc in neighbors:
                            new_r, new_c = r + nr, c + nc
                            if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]) or grid[new_r][new_c] == 0:
                                num_edges += 1
                            elif grid[new_r][new_c] != 2:
                                grid[new_r][new_c] = 2
                                queue.append((new_r, new_c))
                    return num_edges
        return 0


