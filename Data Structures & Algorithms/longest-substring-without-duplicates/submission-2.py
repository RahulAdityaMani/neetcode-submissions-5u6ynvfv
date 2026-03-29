class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        longest = 0
        curr_substring = set(s[l])
        while r < len(s):
            if s[r] in curr_substring:
                curr_substring.remove(s[l])
                l += 1
            else:
                curr_substring.add(s[r])
                if len(curr_substring) > longest:
                    longest = len(curr_substring)
                r += 1
        return longest