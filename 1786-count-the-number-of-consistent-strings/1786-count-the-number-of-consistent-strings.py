class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        return sum(
            True for word in words if all(letter in allowed for letter in word)
        )
