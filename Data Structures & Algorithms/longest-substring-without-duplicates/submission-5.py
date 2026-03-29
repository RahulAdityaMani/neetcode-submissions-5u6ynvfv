class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        longest = 0
        seen = set([s[l]])
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                longest = max(longest, len(seen))
                r += 1
        return longest
