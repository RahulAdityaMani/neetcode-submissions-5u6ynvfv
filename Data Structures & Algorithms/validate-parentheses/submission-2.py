class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                open_parens.append(c)
            else:
                if not open_parens:
                    return False
                last_open = open_parens.pop()
                if c == ")" and last_open != "(":
                    return False
                elif c == "]" and last_open != "[":
                    return False
                elif c == "}" and last_open != "{":
                    return False
        if open_parens:
            return False
        return True