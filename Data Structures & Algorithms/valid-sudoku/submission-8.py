class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for board_i in range(9):
            for board_j in range(9):
                cell = board[board_i][board_j]
                if cell == ".":
                    continue
                else:
                    if cell in row[board_i] or cell in col[board_j] or cell in box[(board_i // 3, board_j // 3)]:
                        return False
                    else:
                        row[board_i].add(cell)
                        col[board_j].add(cell)
                        box[(board_i // 3, board_j // 3)].add(cell)
        return True
