class Solution:
    def moveZeroes(self, numbers: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for index in range(len(numbers)):
            if numbers[index] != 0:
                numbers[non_zero_index], numbers[index] = (
                    numbers[index],
                    numbers[non_zero_index],
                )
                non_zero_index += 1
