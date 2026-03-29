class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        for c in s:
            s_chars[c] = s_chars.get(c, 0) + 1
        t_chars = {}
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1
        if s_chars != t_chars:
            return False
        return True
        