class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                digit = row[j]
                if digit == ".":
                    continue
                box_i = (i // 3) * 3 + j // 3
                if digit in rows[i] or digit in cols[j] or digit in boxes[box_i]:
                    return False
                rows[i].add(digit)
                cols[j].add(digit)
                boxes[box_i].add(digit)
        return True 