class Solution:
    def alternatingSum(self, input_numbers: list[int]) -> int:
        result = 0
        for index, number in enumerate(input_numbers):
            if index % 2 == 0:
                result += number
            else:
                result -= number
        return result