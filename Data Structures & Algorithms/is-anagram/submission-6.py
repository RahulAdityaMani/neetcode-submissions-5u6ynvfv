class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sc_count, tc_count = [0]*26, [0]*26
        for i in range(len(s)):
            sc_count[ord(s[i]) - ord('a')] += 1
            tc_count[ord(t[i]) - ord('a')] += 1
        return tuple(sc_count) == tuple(tc_count)

        