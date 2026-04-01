class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(len(board))]
        boxes = [[] for _ in range(len(board))]
        for i, row in enumerate(board):
            row_set = set()
            for j, digit in enumerate(row):
                if digit in row_set and digit != ".":
                    return False
                cols[j].append(digit)
                # print("Digit:", digit)
                # print("Box:", (i // 3) + (j // 3))
                # print("Box-Row:", i, 3, i // 3)
                # print("Box-Col:", j, 3, j // 3)
                boxes[((i // 3)*3) + (j // 3)].append(digit)
                row_set.add(digit)
        # print(boxes)
        for col in cols:
            col_set = set()
            for digit in col:
                if digit in col_set and digit != ".":
                    return False
                col_set.add(digit)
        for box in boxes:
            box_set = set()
            for digit in box:
                if digit in box_set and digit != ".":
                    return False
                box_set.add(digit)
        return True
        
