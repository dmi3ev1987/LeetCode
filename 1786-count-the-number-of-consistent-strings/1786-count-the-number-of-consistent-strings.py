class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return sum(
            1
            for word in words
            if all(letter in set(allowed) for letter in word)
        )
