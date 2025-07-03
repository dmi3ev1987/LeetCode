class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) < k + 1:
            word += ''.join(
                chr(ord(letter) + 1) if letter != 'z' else 'a'
                for letter in word
            )
        return word[k - 1]