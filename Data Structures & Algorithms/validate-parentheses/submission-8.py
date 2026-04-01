class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(stack,c)
            if c in ["{", "(", "["]:
                stack += [c]
            elif c == "}" and (len(stack) == 0 or not stack[-1] == "{"):
                return False
            elif c == ")" and (len(stack) == 0 or not stack[-1] == "("):
                return False
            elif c == "]" and (len(stack) == 0 or not stack[-1] == "["):
                return False
            else:
                stack = stack[:-1]
        return len(stack) == 0