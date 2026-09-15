class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        k = 0
        while r < len(nums):
            while r < len(nums) and nums[r] != val:
                k += 1
                r += 1
            l = r
            while r < len(nums) and nums[r] == val:
                r += 1
            if r < len(nums):
                k += 1
            if l < len(nums) and r < len(nums):
                nums[l], nums[r] = nums[r], nums[l] 
                r = l
            r += 1
        return k