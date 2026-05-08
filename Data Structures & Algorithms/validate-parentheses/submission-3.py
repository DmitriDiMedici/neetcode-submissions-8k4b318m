class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in pairs:
                if stack:
                    top = stack.pop()
                else:
                    return False

                if pairs[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack