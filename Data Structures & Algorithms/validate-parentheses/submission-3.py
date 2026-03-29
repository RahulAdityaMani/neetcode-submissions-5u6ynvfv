class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                open_parens.append(c)
            elif not open_parens:
                return False
            else:
                last_open = open_parens.pop()
                if c == ")" and not last_open == "(":
                    return False
                elif c == "]" and not last_open == "[":
                    return False
                elif c == "}" and not last_open == "{":
                    return False
        if open_parens:
            return False
        return True