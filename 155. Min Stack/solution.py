class MinStack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((value, value))
        else:
            self.stack.append((value, min(self.stack[-1][1], value)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
