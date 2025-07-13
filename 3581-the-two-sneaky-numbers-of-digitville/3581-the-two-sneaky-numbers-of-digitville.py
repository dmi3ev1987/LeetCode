from collections import Counter


class Solution:
    def getSneakyNumbers(self, numbers: list[int]) -> list[int]:
        return [
            number for number, count in Counter(numbers).items() if count > 1
        ]
