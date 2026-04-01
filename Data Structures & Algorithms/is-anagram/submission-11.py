class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freqs = [0] * 26
        t_freqs = [0] * 26
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            s_freqs[ord(s_char) - ord('a')] += 1
            t_freqs[ord(t_char) - ord('a')] += 1
        return s_freqs == t_freqs