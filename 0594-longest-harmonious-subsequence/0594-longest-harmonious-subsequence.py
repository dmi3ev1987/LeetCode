from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        numbers_counter = Counter(nums)
        max_length = 0

        for number in numbers_counter:
            if number + 1 in numbers_counter:
                max_length = max(
                    max_length,
                    numbers_counter[number] + numbers_counter[number + 1],
                )

        return max_length
