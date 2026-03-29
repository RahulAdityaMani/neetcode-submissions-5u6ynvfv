class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            anagram_key = [0]*26
            for c in s:
                anagram_key[ord(c) - ord('a')] += 1
            anagram_dict[tuple(anagram_key)].append(s)
        return list(anagram_dict.values())