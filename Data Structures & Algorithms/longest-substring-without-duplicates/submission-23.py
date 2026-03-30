class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len < 2:
            return s_len
        left = 0
        seen = { s[left]: left }
        max_len = 1
        for right in range(1, len(s)):
            if s[right] in seen and left <= seen[s[right]]:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        return max_len

