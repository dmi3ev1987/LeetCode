from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()  # Основная очередь, хранит элементы в порядке стека
        self.q2 = deque()  # Вспомогательная очередь для операции push

    def push(self, x: int) -> None:
        # 1. Перемещаем новый элемент в q2
        self.q2.append(x)
        # 2. Перемещаем все элементы из q1 в q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # 3. Меняем q1 и q2 местами,
        # q1 теперь содержит все элементы в правильном порядке стека
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if not self.empty():
            return self.q1.popleft()
        return None  # Или бросить исключение

    def top(self) -> int:
        if not self.empty():
            return self.q1[0]
        return None  # Или бросить исключение

    def empty(self) -> bool:
        return not self.q1
