class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        if len(s) < 2:
            return len(s)
        # k needed = window size - max freq char count in window
        char_counts = {}
        l = 0
        char_counts[s[l]] = 1
        max_freq = 1
        max_len = 1
        for r in range(1, len(s)):
            candidate = s[r]
            char_counts[candidate] = char_counts.get(candidate, 0) + 1
            max_freq = max(max_freq, char_counts[candidate])
            window_size = r - l + 1
            while window_size - max_freq > k:
                char_counts[s[l]] -= 1
                l += 1
                window_size = r - l + 1
            max_len = max(max_len, window_size)
        return max_len

