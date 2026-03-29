class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) < k:
            return len(s)
        left, right = 0, 1
        curr_freqs = { s[left]: 1 }
        max_freq = 1
        max_len = 1
        moved_right = True
        while right < len(s):
           # print("left", left, "right", right, "window:", s[left:right+1], "window_size", right - left + 1, "curr_freqs", curr_freqs, "max_freq", max_freq, "max_len", max_len)
            if moved_right:
                curr_freqs[s[right]] = curr_freqs.get(s[right], 0) + 1
                for c in curr_freqs: # 26 -- constant
                    max_freq = max(max_freq, curr_freqs[c])
            window_size = right - left + 1
            if window_size - max_freq > k:
                curr_freqs[s[left]] -= 1
                for c in curr_freqs: # 26 -- constant
                    max_freq = max(max_freq, curr_freqs[c])
                left += 1
                moved_right = False
            else:
                max_len = max(max_len, window_size)
                right += 1
                moved_right = True
        return max_len
# AABABBA k = 1
# left = 0, freqs: A = 1, max_freq = 1, max_len = 1
# AA left = 0, right = 1, freqs: A = 2, max_freq = 2, window = 2, max_len = 2
# AAB left = 0, right = 2, freqs: A = 2 B = 1, max_freq = 2, window = 3, max_len = 3
# AABA left = 0, right = 3, freqs: A = 3 B = 1, max_freq = 3, window = 4, max_len = 4
# AABAB left = 0, right = 4, freqs: A = 3 B = 2, max_freq = 3, window = 5, 5-3>k=2 -> freqs: A = 2 B = 2, left = 1
# ABAB left = 1, right = 4, freqs: 

