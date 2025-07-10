class Solution:
    def minimumOperations(self, input_numbers: list[int]) -> int:
        return sum(1 for number in input_numbers if number % 3)
