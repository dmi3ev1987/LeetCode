class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = map(lambda word: sum(weights[ord(char) - ord('a')] for char in word) % 26, words)
        result = map(lambda x: chr(ord('z') - x), result)
        return ''.join(result)
        