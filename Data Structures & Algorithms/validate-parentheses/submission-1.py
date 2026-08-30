class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if len(stack) > 0 and stack[-1] == "(" and s[i] == ")":
                stack.pop()
            elif len(stack) > 0 and stack[-1] == "[" and s[i] == "]":
                stack.pop()
            elif len(stack) > 0 and stack[-1] == "{" and s[i] == "}":
                stack.pop()
            else:
                stack.append(s[i])
            
        return True if len(stack) == 0 else False