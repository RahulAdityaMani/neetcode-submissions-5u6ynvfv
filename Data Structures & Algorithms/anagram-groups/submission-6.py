class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            char_counts = [0] * 26
            for c in s:
                char_counts[ord(c) - ord('a')] += 1
            char_counts_key = tuple(char_counts)
            if char_counts_key in anagrams:
                anagrams[char_counts_key].append(s)
            else:
                anagrams[char_counts_key] = [s]
        return list(anagrams.values())
        