class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp_stack = []

    def push(self, value: int) -> None:
        while self.stack:
            self.temp_stack.append(self.stack.pop())
        self.temp_stack.append(value)
        while self.temp_stack:
            self.stack.append(self.temp_stack.pop())

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
        return None

    def peek(self) -> int:
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self) -> bool:
        return not self.stack
