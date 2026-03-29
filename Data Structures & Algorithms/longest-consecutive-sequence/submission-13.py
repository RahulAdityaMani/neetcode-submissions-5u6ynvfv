class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num + 1
                length = 1
                while curr in nums_set:
                    curr += 1
                    length += 1
                longest = max(length, longest)
        return longest