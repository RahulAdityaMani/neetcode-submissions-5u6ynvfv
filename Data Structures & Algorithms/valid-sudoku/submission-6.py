class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            row_set = set()
            for cell in row:
                if cell == ".":
                    continue
                elif cell in row_set:
                    return False
                row_set.add(cell)

        for col_i in range(9):
            col = set()
            for i in range(9):
                cell = board[i][col_i]
                if cell == ".":
                    continue
                if cell in col:
                    return False
                col.add(cell)

        for box_i in range(9):
            box = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    r = (box_i // 3) * 3 + i
                    c = (box_i % 3) * 3 + j
                    cell = board[r][c]
                    if cell == ".":
                        continue
                    if cell in box:
                        return False
                    box.add(cell)

        return True