class Solution:
    def leftRightDifference(self, numbers: list[int]) -> list[int]:
        return [
            abs(sum(numbers[index + 1 :]) - sum(numbers[:index]))
            for index in range(len(numbers))
        ]
