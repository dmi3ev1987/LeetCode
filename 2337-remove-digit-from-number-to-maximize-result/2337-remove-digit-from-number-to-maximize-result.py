class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = "0"
        
        for i in range(len(number)):
            if number[i] == digit:
                current_number = number[:i] + number[i+1:]
                if current_number > max_number:
                    max_number = current_number
        
        return max_number
