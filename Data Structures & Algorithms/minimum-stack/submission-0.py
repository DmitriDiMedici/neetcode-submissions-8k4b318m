class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp_stack = []
        min_val = self.stack[-1]

        while len(self.stack):
            min_val = min(min_val, self.stack[-1])
            temp_stack.append(self.stack.pop())

        while len(temp_stack):
            self.stack.append(temp_stack.pop())

        return min_val