class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        opts = set()
        first = strs[0]
        for i in range(len(first)):
            for s in strs:
                if i >= len(s) or s[i] != first[i]:
                    return first[0:i]
        return first



