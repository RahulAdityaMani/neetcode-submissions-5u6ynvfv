class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                else:
                    if cell in seen:
                        return False
                    else:
                        seen.add(cell)
        
        for col_i in range(9):
            seen = set()
            for row_i in range(9):
                cell = board[row_i][col_i]
                if cell == ".":
                    continue
                else:
                    if cell in seen:
                        return False
                    else:
                        seen.add(cell)
        
        for box in range(9):
            seen = set()
            for box_i in range(0, 3):
                for box_j in range(0, 3):
                    board_row = box // 3
                    board_col = box % 3
                    row_i = board_row * 3 + box_i
                    col_i = board_col * 3 + box_j
                    cell = board[row_i][col_i]
                    if cell == ".":
                        continue
                    else:
                        if cell in seen:
                            return False
                        else:
                            seen.add(cell)
        return True