class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for c in s:
            if c in s_chars:
                s_chars[c] += 1
            else:
                s_chars[c] = 1
        t_chars = {}
        for c in t:
            if c in t_chars:
                t_chars[c] += 1
            else:
                t_chars[c] = 1
        if s_chars != t_chars:
            return False
        return True
        