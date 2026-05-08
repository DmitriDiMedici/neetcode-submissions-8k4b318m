class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                if not stack:
                    return False

                top = stack.pop()
                if pairs[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack