class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        index_list = [
            [index, int(number)] for index, number in enumerate(boxes)
        ]
        result = []
        for index, number in index_list:
            operstions = 0
            for inner_index, inner_number in index_list:
                if inner_index == index:
                    continue
                if inner_number == 1:
                    operstions += abs(index - inner_index)
            result.append(operstions)
        return result