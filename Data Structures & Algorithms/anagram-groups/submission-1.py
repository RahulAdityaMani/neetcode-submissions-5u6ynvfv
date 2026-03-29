class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            anagram_key = ''.join(sorted(s))
            if anagram_key in anagrams:
                anagrams[anagram_key].append(s)
            else:
                anagrams[anagram_key] = [s]
        return list(anagrams.values())