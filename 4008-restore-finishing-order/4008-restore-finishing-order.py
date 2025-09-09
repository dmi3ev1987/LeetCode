class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        return [id for id in order if id in friends]
