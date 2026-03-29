class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        anagram = [0] * 26
        for i in range(len(s)):
            anagram[ord(s[i]) - ord('a')] += 1
            anagram[ord(t[i]) - ord('a')] -= 1
        return all(v == 0 for v in anagram)

        