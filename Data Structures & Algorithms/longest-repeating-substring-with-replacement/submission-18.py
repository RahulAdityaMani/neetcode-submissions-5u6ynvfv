class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_len = len(s)
        if s_len < 2:
            return s_len
        left = 0
        freqs = { s[left]: 1 }
        max_freq = 1
        max_len = 1
        for right in range (1, s_len):
            curr_len = right - left + 1
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            max_freq = max(max_freq, freqs[s[right]])
            if curr_len - max_freq > k:
                while curr_len - max_freq > k:
                    freqs[s[left]] -= 1
                    left += 1
                    curr_len = right - left + 1
            max_len = max(max_len, curr_len)
        return max_len