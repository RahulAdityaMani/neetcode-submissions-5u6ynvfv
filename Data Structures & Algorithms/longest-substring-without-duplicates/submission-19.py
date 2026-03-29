class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        last_seen = {}
        l, r = 0, 1
        last_seen[s[l]] = l
        max_len = 1
        while r < len(s):
            if s[r] in last_seen and last_seen[s[r]] >= l:
                l = last_seen[s[r]] + 1
            last_seen[s[r]] = r
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
