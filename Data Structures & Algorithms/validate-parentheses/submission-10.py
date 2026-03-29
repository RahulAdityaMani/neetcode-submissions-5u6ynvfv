class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(c, "stack: ", stack)
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif stack:
                prev_bracket = stack.pop()
                if (prev_bracket == "{" and c != "}") or (prev_bracket == "[" and c != "]") or (prev_bracket == "(" and c != ")"):
                    return False
            else:
                return False
        if stack:
            return False
        return True