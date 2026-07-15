class MinStack:

    def __init__(self):
        self.stack = []
        self.side_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.side_stack or val <= self.side_stack[-1]:
            self.side_stack.append(val)

    def pop(self) -> None:
        var = self.stack.pop()
        if var == self.side_stack[-1]:
            self.side_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        smallest = self.side_stack[-1]
        return smallest
