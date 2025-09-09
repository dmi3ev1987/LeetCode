class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        result = []
        for id in order:
            if id in friends:
                result.append(id)
        return result
