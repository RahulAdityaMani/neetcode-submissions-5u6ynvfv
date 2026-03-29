class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            anagram_key = str(sorted(s))
            if anagram_key in anagrams:
                anagrams[anagram_key].append(s)
            else:
                anagrams[anagram_key] = [s]
        output = []
        for anagram_key in anagrams:
            output.append(anagrams[anagram_key])
        return output