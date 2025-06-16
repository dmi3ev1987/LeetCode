class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_divisible_m = 0
        sum_not_divisible_m = 0
        for number in range(1, n + 1):
            if number % m == 0:
                sum_divisible_m += number
            else:
                sum_not_divisible_m += number
        return sum_not_divisible_m - sum_divisible_m
