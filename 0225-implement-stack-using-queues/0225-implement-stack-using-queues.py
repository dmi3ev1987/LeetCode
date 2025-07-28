from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, value: int) -> None:
        self.stack.appendleft(value)

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