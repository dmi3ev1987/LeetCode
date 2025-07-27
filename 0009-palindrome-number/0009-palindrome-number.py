class Solution:
    def isPalindrome(self, number: int) -> bool:
        reversed_number = 0
        number_copy = number

        while number_copy > 0:
            last_digit = number_copy % 10
            reversed_number = reversed_number * 10 + last_digit
            number_copy //= 10

        return number == reversed_number
