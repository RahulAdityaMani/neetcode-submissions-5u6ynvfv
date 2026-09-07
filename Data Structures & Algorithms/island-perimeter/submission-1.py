class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = deque([(i, j)])
                    grid[i][j] = 2
                    num_edges = 0
                    while queue:
                        r, c = queue.popleft()
                        if  (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0):
                            num_edges += 1
                        elif (r == i and c == j) or grid[r][c] != 2:
                            grid[r][c] = 2
                            if r + 1 != i or c != j:
                                queue.append((r + 1, c))
                            if r - 1 != i or c != j:
                                queue.append((r - 1, c))
                            if r != i or c + 1 != j:
                                queue.append((r, c + 1))
                            if r != i or c - 1 != j:
                                queue.append((r, c - 1))
                    return num_edges
        return 0


