class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1
        max_len = 1
        left, right = 0, 1
        last_seen = { s[left]: left }
        while right < len(s):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1
            last_seen[s[right]] = right
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
            right += 1
        return max_len