class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            s_char_counts = defaultdict(int)
            for c in s:
                s_char_counts[c] += 1
            key = frozenset(s_char_counts.items())
            anagrams[key].append(s)

        return list(anagrams.values())