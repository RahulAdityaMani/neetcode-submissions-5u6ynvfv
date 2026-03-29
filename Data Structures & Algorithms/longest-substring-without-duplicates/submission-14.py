class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_set = set()
        l, r = 0, 1
        max_len = 1
        char_set.add(s[l])
        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len, r - l + 1)
            else:
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return max_len