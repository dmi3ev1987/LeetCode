from collections import Counter


class Solution:
    def maxDistinct(self, input_string: str) -> int:
        return len(Counter(input_string))
