class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_count = [0]*26
        for i in range(len(s)):
            c_count[ord(s[i]) - ord('a')] += 1
            c_count[ord(t[i]) - ord('a')] -= 1
        for c in c_count:
            if c != 0:
                return False
        return True

        