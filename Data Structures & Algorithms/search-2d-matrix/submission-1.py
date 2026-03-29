class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        candidate_row = []
        for i in range(len(matrix) - 1):
            if matrix[i][0] <= target and matrix[i + 1][0] > target:
                candidate_row = matrix[i]
        if not candidate_row:
            if matrix[-1][0] <= target:
                candidate_row = matrix[-1]
            else:
                return False
        
        l, r = 0, len(candidate_row) - 1
        while l <= r:
            m = l + (r - l) // 2
            if candidate_row[m] == target:
                return True
            elif candidate_row[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return False