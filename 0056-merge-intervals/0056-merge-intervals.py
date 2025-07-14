class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for current_array in intervals[1:]:
            last_array = result[-1]
            if current_array[0] <= last_array[-1]:
                last_array[-1] = max(last_array[-1], current_array[-1])
            else:
                result.append(current_array)
        return result