from collections import Counter

class Solution:
    def maxFreqSum(self, input_string: str) -> int:
        vowels = 'aeiou'
        max_vowels = 0
        max_consonants = 0 
        for key, value in Counter(input_string).items():
            if key in vowels:
                max_vowels = max(value, max_vowels)
            else:
                max_consonants = max(value, max_consonants)
        return max_vowels + max_consonants