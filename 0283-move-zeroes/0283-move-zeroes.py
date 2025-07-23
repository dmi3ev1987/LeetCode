class Solution:
    def moveZeroes(self, numbers: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] == 0:
                numbers.append(numbers.pop(left))
                right -= 1
            else:
                left += 1