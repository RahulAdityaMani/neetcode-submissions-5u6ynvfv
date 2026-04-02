class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        combo = []
        sorted_candidates = sorted(candidates)
        def dfs(i: int, curr_sum: int):
            if curr_sum == target:
                output.append(combo.copy())
                return
            if curr_sum > target:
                return
            if i == len(sorted_candidates):
                return
            j = i + 1
            while j < len(sorted_candidates) and sorted_candidates[i] == sorted_candidates[j]:
                j += 1
            dfs(j, curr_sum)
            combo.append(sorted_candidates[i])
            dfs(i + 1, curr_sum + sorted_candidates[i])
            combo.pop()
        dfs(0, 0)
        return output