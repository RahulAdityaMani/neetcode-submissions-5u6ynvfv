class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        longest = 0
        seen = { s[l]: l }
        for r in range(1, len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            curr = r - l + 1
            longest = max(longest, curr)
            seen[s[r]] = r
        return longest
