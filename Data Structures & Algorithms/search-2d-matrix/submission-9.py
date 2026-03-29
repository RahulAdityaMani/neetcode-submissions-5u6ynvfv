class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                candidate = matrix[m]
                lc = 0
                rc = len(candidate) - 1
                while lc <= rc:
                    mc = lc + ((rc - lc) // 2)
                    if candidate[mc] == target:
                        return True
                    elif candidate[mc] > target:
                        rc = mc - 1
                    else:
                        lc = mc + 1
                return False
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        return False