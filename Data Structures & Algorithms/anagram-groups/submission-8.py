class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_dict = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            groups_dict[key].append(s)
        return list(groups_dict.values())