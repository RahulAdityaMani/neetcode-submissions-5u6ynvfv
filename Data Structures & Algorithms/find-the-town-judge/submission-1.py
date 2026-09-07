class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustees = defaultdict(int)
        trusters = defaultdict(int)
        for relationship in trust:
            truster, trustee = relationship[0], relationship[1]
            trustees[trustee] += 1
            trusters[truster] += 1
        for i in range(1, n + 1):
            if trustees[i] == n - 1 and trusters[i] == 0:
                return i
        return -1
