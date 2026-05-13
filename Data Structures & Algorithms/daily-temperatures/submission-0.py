class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temperature, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return res