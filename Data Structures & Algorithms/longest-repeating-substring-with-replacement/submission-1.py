class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        l, r, max_occurring, longest_window = 0, 1, 1, 1
        window_chars = defaultdict(int)
        window_chars[s[l]] = 1
        window_size = 1
        while r < len(s):
            window_size = r - l + 1
            curr_char_count = window_chars[s[r]] + 1
            max_occurring = max(max_occurring, curr_char_count)
            if window_size - max_occurring <= k:
                window_chars[s[r]] = curr_char_count
                longest_window = max(longest_window, window_size)
                r += 1
            else:
                window_chars[s[l]] -= 1
                l += 1
        return longest_window