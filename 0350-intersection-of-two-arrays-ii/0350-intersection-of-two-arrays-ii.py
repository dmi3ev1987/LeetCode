class Solution:
    def intersect(self, numbers1: list[int], numbers2: list[int]) -> list[int]:
        result = []
        for number in numbers1:
            if number in numbers2:
                result.append(number)
                numbers2.remove(number)
        return result
