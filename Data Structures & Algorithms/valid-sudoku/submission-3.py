class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(board: List[List[str]]) -> bool:
            for row in board:
                dupes = set()
                for cell in row:
                    if cell == ".":
                        continue
                    if cell in dupes:
                        return False
                    dupes.add(cell)
            return True
        
        cols = []
        for i in range(9):
            curr_col = []
            for j in range(9):
                curr_col.append(board[j][i])
            cols.append(curr_col)
        
        boxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                box_lst = [cell for row in box for cell in row]
                boxes.append(box_lst)

        return valid(board) and valid(cols) and valid(boxes)
