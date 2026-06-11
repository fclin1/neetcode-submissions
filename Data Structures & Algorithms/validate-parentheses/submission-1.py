class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in (")", "]", "}"):
                if not stack:
                    return False
                top = stack.pop()
                if c == ")" and top != "(":
                    return False
                elif c == "]" and top != "[":
                    return False
                elif c == "}" and top != "{":
                    return False
            else:
                stack.append(c)
        return len(stack) == 0