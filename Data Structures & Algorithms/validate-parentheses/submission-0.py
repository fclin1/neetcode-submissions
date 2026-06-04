class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Match = {')' : '(', ']' : '[', '}' : '{'}
        for c in s:
            if c not in Match:
                stack.append(c)
            else:
                if not stack or stack[-1] != Match[c]:
                    return False
                stack.pop()
        
        return not stack
        