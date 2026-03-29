class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        l, r, max_occurring, longest_window = 0, 1, 1, 1
        window_chars = defaultdict(int)
        window_chars[s[l]] = 1
        for r in range(1, len(s)):
            window_chars[s[r]] += 1
            max_occurring = max(max_occurring, window_chars[s[r]])
            while (r - l + 1) - max_occurring > k:
                window_chars[s[l]] -= 1
                l += 1
            longest_window = max(longest_window, r - l + 1)
                
        return longest_window