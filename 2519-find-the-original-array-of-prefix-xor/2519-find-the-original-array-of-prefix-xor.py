class Solution:
    def findArray(self, input_array: list[int]) -> list[int]:
        length = len(input_array)
        result = [0] * length
        result[0] = input_array[0]
        for index in range(1, length):
            result[index] = input_array[index] ^ input_array[index - 1]
        return result