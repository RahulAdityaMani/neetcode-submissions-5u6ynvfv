class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    queue = deque([(i, j)])
                    curr_area = 1
                    while queue:
                        node_i, node_j = queue.popleft()
                        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        for x, y in offsets:
                            r, c = node_i + x, node_j + y
                            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                                continue
                            grid[r][c] = 0
                            queue.append((r, c))
                            curr_area += 1
                    max_area = max(max_area, curr_area)
        return max_area
