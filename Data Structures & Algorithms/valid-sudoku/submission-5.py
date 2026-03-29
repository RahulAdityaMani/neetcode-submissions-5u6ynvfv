class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(rows: List[List[str]]) -> bool:
            for row in rows:
                row_set = set()
                for cell in row:
                    if cell == ".":
                        continue
                    elif cell in row_set:
                        return False
                    row_set.add(cell)
            return True
        cols = []
        for col_i in range(9):
            col = []
            for i in range(9):
                col.append(board[i][col_i])
            cols.append(col)
        boxes = []
        for box_i in range(9):
            box = []
            for i in range(0, 3):
                for j in range(0, 3):
                    r = (box_i // 3) * 3 + i
                    c = (box_i % 3) * 3 + j
                    box.append(board[r][c])
            boxes.append(box)
        return valid(board) and valid(cols) and valid(boxes)