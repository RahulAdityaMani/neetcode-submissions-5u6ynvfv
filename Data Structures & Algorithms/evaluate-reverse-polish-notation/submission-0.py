class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = []
        for token in tokens:
            if token == "+":
                n2 = operations.pop()
                n1 = operations.pop()
                res = n1 + n2
                operations.append(res)
            elif token == "-":
                n2 = operations.pop()
                n1 = operations.pop()
                res = n1 - n2
                operations.append(res)
            elif token == "*":
                n2 = operations.pop()
                n1 = operations.pop()
                res = n1 * n2
                operations.append(res)
            elif token == "/":
                n2 = operations.pop()
                n1 = operations.pop()
                res = int(n1 / n2)
                operations.append(res)
            else:
                operations.append(int(token))
        return operations.pop()