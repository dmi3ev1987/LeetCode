class MyStack:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, value: int) -> None:
        self.temp.append(value)
        while self.stack:
            self.temp.append(self.stack.pop(0))
        self.stack, self.temp = self.temp, self.stack

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(0)
        return None

    def top(self) -> int:
        if not self.empty():
            return self.stack[0]
        return None

    def empty(self) -> bool:
        return not self.stack
