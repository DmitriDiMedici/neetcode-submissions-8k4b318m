class MinStack:
    def __init__(self):
        self.stack = []
        self.minimals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimals.append(val if not self.minimals else min(val, self.minimals[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minimals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimals[-1]