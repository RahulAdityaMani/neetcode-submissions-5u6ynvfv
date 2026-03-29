class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)
        while l < r:
            m = l + ((r - l) // 2)
            if matrix[m][0] > target:
                r = m
            else:
                l = m + 1
        if l > 0:
            candidate_row = matrix[l-1]
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