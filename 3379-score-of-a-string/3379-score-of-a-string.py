class Solution:
    def scoreOfString(self, input_string: str) -> int:
        result = 0
        ascii_values = [ord(letter) for letter in input_string]
        for index in range(len(input_string) - 1):
            result += abs(ascii_values[index] - ascii_values[index+1])
        return result