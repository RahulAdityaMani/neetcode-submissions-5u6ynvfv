class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        parens_stack = []
        def helper(num_open: int, num_close: int):
            if num_open == n and num_close == n:
                results.append("".join(parens_stack))
            else:
                if num_open < n:
                    parens_stack.append("(")
                    helper(num_open + 1, num_close)
                    parens_stack.pop()
                if num_close < num_open:
                    parens_stack.append(")")
                    helper(num_open, num_close + 1)
                    parens_stack.pop()
        helper(0, 0)
        return results