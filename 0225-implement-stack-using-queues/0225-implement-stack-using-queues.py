from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()
        self.temp = deque()

    def push(self, value: int) -> None:
        self.temp.append(value)
        for _ in range(len(self.stack)):
            self.temp.append(self.stack.popleft())
        self.stack, self.temp = self.temp, self.stack


    def pop(self) -> int:
        if not self.empty():
            return self.stack.popleft()
        return None

    def top(self) -> int:
        if not self.empty():
            return self.stack[0]
        return None

    def empty(self) -> bool:
        return not self.stack