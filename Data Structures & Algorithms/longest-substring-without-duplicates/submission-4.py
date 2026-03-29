class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        longest = 0
        curr_len = 1
        last_seen = { s[l]: l }
        while r < len(s):
            print(s[l:r+1])
            if s[r] in last_seen:
                l = max(l, last_seen[s[r]] + 1)
            last_seen[s[r]] = r
            curr_len = r - l + 1
            longest = max(longest, curr_len)
            r += 1
        return longest
                