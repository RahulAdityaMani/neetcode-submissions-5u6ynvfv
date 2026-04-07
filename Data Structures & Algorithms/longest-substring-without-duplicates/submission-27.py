class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1
        max_len = 1
        l = 0
        r = l + 1
        curr_len = 1
        curr_set = set()
        curr_set.add(s[l])
        while r < len(s):
            if s[r] in curr_set:
                while s[r] in curr_set:
                    curr_set.remove(s[l])
                    curr_len -= 1
                    l += 1
                curr_set.add(s[r])
                curr_len += 1
            else:
                curr_len += 1
                curr_set.add(s[r])
                max_len = max(max_len, curr_len)
            r += 1
        return max_len

