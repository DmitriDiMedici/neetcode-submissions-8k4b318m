class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for km, sp in cars:
            time = (target - km) / sp
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)