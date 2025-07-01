from collections import Counter


class Solution:
    def find_even_numbers(self, digits: list[int]) -> list[int]:
        result = []
        digits_count = Counter(
            digits,
        )
        for number in range(100, 1000, 2):
            number_count = Counter([int(digit) for digit in str(number)])
            if all(
                digits_count[digit] >= number_count[digit]
                for digit in number_count
            ):
                result.append(number)
        return result
