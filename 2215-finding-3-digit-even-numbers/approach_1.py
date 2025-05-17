class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        numbers_set = set()
        length = len(digits)
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i == j or j == k or i == k:
                        continue
                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if number >= 100 and number % 2 == 0:
                        numbers_set.add(number)
        return sorted(list(numbers_set))
