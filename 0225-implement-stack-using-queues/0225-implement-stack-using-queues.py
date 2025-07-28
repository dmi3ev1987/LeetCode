class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(-1)
        return None
        

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]
        return None
        

    def empty(self) -> bool:
        return not self.stack