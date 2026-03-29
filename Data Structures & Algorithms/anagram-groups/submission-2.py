class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            an_key = [0]*26
            for c in s:
                an_key[ord(c) - ord('a')] += 1
            anagrams[tuple(an_key)].append(s)
        return list(anagrams.values())