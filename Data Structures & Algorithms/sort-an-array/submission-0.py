class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 5 2 3 4 1
        # 5 2  3 4 1
        # 2
        def sortHelper(left, right):
            if len(left) > 1:
                left = sortHelper(left[:len(left)//2], left[len(left)//2:])
            if len(right) > 1:
                right = sortHelper(right[:len(right)//2], right[len(right)//2:])
            l, r = 0, 0
            sortedArray = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    sortedArray.append(left[l])
                    l += 1
                else:
                    sortedArray.append(right[r])
                    r += 1
            while l < len(left):
                sortedArray.append(left[l])
                l += 1
            while r < len(right):
                sortedArray.append(right[r])
                r += 1
            return sortedArray

        return sortHelper(nums[:len(nums)//2], nums[len(nums)//2:])
            
