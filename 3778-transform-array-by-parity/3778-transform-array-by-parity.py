class Solution:
    def transformArray(self, numbers: list[int]) -> list[int]:
        return sorted(1 if number % 2 else 0 for number in numbers)
