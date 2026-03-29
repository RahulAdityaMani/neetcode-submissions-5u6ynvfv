class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        l, r = 0, 1
        char_counts = [0] * 26
        char_counts[ord(s[l]) - ord('A')] += 1
        max_freq = 1
        max_len = 0
        while r < len(s):
            char_counts[ord(s[r]) - ord('A')] += 1
            max_freq = max(max_freq, char_counts[ord(s[r]) - ord('A')])
            curr_window = r - l + 1 # inclusive
            if curr_window - max_freq > k:
                char_counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len