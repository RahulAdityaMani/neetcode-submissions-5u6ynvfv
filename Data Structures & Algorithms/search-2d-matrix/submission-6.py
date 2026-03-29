class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        while l < r:
            m = l + ((r - l) // 2)
            if matrix[m][-1] >= target:
                r = m
            else:
                l = m + 1
        if l < len(matrix):
            candidate_row = matrix[l]
            l = 0
            r = len(candidate_row) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if candidate_row[m] == target:
                    return True
                elif candidate_row[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False