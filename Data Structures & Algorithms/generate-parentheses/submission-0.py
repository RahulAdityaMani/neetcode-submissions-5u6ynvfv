class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def helper(prefix: str, num_open: int, num_close: int):
            if num_open == n and num_close == n:
                results.append(prefix)
            elif num_open >= num_close:
                if num_open < n:
                    helper("".join([prefix, "("]), num_open + 1, num_close)
                helper("".join([prefix, ")"]), num_open, num_close + 1)
        helper("", 0, 0)
        return results