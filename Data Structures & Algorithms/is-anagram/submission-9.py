class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        _s, _t = [0]*26, [0]*26
        for i in range(len(s)):
            _s[ord(s[i]) - ord('a')] += 1
            _t[ord(t[i]) - ord('a')] += 1
        return tuple(_s) == tuple (_t)
        