class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) <= k:
            return len(s)
        left = 0
        freqs = { s[left]: 1 }
        max_freq = 1
        max_len = 1
        for right in range(1, len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            max_freq = max(max_freq, freqs[s[right]])
            window_size = right - left + 1
            while window_size - max_freq > k:
                freqs[s[left]] -= 1
                left += 1
                window_size = right - left + 1
            max_len = max(max_len, window_size)
        return max_len