class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        candidate_row = []
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + (r - l) // 2
            print(l, m, r)
            if (
                m == r and matrix[m][0] <= target
            ) or (
                m + 1 <= r and matrix[m][0] <= target and matrix[m + 1][0] > target
            ):
                candidate_row = matrix[m]
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        print(candidate_row)
        if not candidate_row:
            return False
        
        l, r = 0, len(candidate_row) - 1
        while l <= r:
            m = l + (r - l) // 2
            if candidate_row[m] == target:
                return True
            elif candidate_row[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False