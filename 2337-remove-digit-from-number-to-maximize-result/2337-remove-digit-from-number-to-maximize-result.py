class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = "0"
        
        for i in range(len(number)):
            if number[i] == digit:
                current = number[:i] + number[i+1:]
                if current > max_number:
                    max_number = current
        
        return max_number