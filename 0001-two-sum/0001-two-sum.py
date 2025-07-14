class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        length = len(numbers)
        for index in range(length):
            for inner_index in range(length):
                if index == inner_index:
                    continue
                if numbers[index] + numbers[inner_index] == target:
                    return [index, inner_index]
        return None
