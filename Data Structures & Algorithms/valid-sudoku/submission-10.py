class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]
        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit == ".":
                    continue
                if digit in rows[i] or digit in cols[j] or digit in boxes[(i // 3) * 3 + (j // 3)]:
                    return False
                rows[i].add(digit)
                cols[j].add(digit)
                boxes[(i // 3) * 3 + (j // 3)].add(digit)
        # print(rows)
        # print(cols)
        # print(boxes)
        # 1 2 . | . 3 . | . . .
        # 4 . . | 5 . . | . . .
        # . 9 1 | . . . | . . 3
        # ---------------------
        # 5 . . | . 6 . | . . 4
        # . . . | 8 . 3 | . . 5
        # 7 . . | . 2 . | . . 6
        # ---------------------
        # . . . | . . . | 2 . .
        # . . . | 4 1 9 | . . 8
        # . . . | . 8 . | . 7 9
        return True