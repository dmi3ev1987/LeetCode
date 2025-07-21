class Solution:
    def kidsWithCandies(self, candies: list[int], extra_candies: int) -> list[bool]:
        return [kid + extra_candies >= max(candies) for kid in candies]