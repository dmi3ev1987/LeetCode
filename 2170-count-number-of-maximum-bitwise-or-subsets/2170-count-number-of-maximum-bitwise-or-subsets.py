from itertools import combinations


class Solution:
    def countMaxOrSubsets(self, numbers: list[int]) -> int:
        subsets = [
            list(combination)
            for subset_size in range(1, len(numbers) + 1)
            for combination in combinations(numbers, subset_size)
        ]
        max_bitwise_or = 0
        for number in numbers:
            max_bitwise_or |= number
        count = 0
        for subset in subsets[:-1]:
            current_bitwise_or = 0
            for number in subset:
                current_bitwise_or |= number
            if current_bitwise_or == max_bitwise_or:
                count += 1
        return count + 1