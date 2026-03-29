class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_set = set()
        l, r = 0, 1
        max_len = 1
        char_set.add(s[l])
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            r += 1
            max_len = max(max_len, r - l)
        return max_len