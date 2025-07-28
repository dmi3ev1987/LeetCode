class MyStack:
    def __init__(self):
        self.queue = []
        self.temp_queue = []

    def push(self, value: int) -> None:
        self.temp_queue.append(value)
        while self.queue:
            self.temp_queue.append(self.queue.pop(0))
        self.queue, self.temp_queue = self.temp_queue, self.queue

    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)
        return None

    def top(self) -> int:
        if not self.empty():
            return self.queue[0]
        return None

    def empty(self) -> bool:
        return len(self.queue) == 0
