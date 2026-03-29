class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagram_groups[tuple(key)].append(s)
        return list(anagram_groups.values())