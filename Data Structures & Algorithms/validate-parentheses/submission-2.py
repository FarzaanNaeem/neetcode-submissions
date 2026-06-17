class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ('(', '{', '['):
                stack.append(p)
            else:
                if len(stack) > 0:
                    if p == ')' and stack[-1] != '(':
                        return False
                    if p == '}' and stack[-1] != '{':
                        return False
                    if p == ']' and stack[-1] != '[':
                        return False
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False