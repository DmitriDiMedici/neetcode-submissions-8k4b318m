class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in pairs:
                stack.append(char)
            elif char in pairs.values():
                if not stack:
                    return False

                top = stack.pop()
                if pairs[top] != char:
                    return False

        return not stack