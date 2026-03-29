class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l = 0
        r = len(matrix)
        while l < r:
            m = l + ((r - l) // 2)
            if matrix[m][-1] >= target:
                r = m
            else:
                l = m + 1
        if l < len(matrix):
            candidate = matrix[l]
            lc = 0
            rc = len(candidate)
            while lc < rc:
                mc = lc + ((rc - lc) // 2)
                if candidate[mc] >= target:
                    rc = mc
                else:
                    lc = mc + 1
            if lc < len(candidate) and candidate[lc] == target:
                    return True
        return False