class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def helper(l, r):
            len_total_arr = r - l
            if len_total_arr <= 1:
                return [nums[l]]
            mid_total_arr = l + len_total_arr // 2
            left_arr = helper(l, mid_total_arr)
            right_arr = helper(mid_total_arr, r)
            l, r, merged = 0, 0, []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] < right_arr[r]:
                    merged.append(left_arr[l])
                    l += 1
                else:
                    merged.append(right_arr[r])
                    r += 1
            while l < len(left_arr):
                merged.append(left_arr[l])
                l += 1
            while r < len(right_arr):
                merged.append(right_arr[r])
                r += 1
            return merged
        return helper(0, len(nums))


