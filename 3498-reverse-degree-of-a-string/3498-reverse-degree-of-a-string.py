class Solution:
    def reverseDegree(self, input_string: str) -> int:
        degree = 0
        for index in range(len(input_string)):
            reversed_index = 26 - (ord(input_string[index]) - ord('a'))
            degree += (index + 1) * reversed_index
        return degree
