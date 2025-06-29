class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        enumerated_list = [
            [index, int(number)] for index, number in enumerate(boxes)
        ]
        result = []
        for index, number in enumerated_list:
            operations = 0
            for inner_index, inner_number in enumerated_list:
                if inner_index == index:
                    continue
                if inner_number == 1:
                    operations += abs(index - inner_index)
            result.append(operations)
        return result