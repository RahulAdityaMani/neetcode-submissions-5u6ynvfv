class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = list(strs[0])
        for s in strs:
            i = 0
            while i < min(len(first), len(s)):
                if first[i] != s[i]:
                    break
                i += 1
            first = first[:i]
        return "".join(first)



