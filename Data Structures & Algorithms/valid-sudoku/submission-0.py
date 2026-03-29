class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validRows(rows: List[List[str]]):
            for row in rows:
                row_set = set()
                for cell in row:
                    if cell in row_set and cell != ".":
                        return False
                    row_set.add(cell)
            return True
        validRows(board)
        cols_list = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cols_list[j].append(board[i][j])
        validRows(cols_list)
        boxes = []
        for i in range (0, 9, 3):
            for j in range(0, 9, 3):
                box = [row[j:j+3] for row in board[i:i+3]]
                box_lst = [cell for row in box for cell in row]
                boxes.append(box_lst)
        return validRows(board) and validRows(cols_list) and validRows(boxes)
