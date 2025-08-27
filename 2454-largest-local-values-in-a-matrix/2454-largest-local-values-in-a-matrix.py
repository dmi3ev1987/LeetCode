class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        length = len(grid) - 2
        result = []
        for level in range(length):
            matrix = []
            row_to_insert = []
            for index in range(length):
                matrix.extend(grid[level][index : index + 3])
                matrix.extend(grid[level + 1][index : index + 3])
                matrix.extend(grid[level + 2][index  :index + 3])
                row_to_insert.append(max(matrix))
                matrix = []
            result.append(row_to_insert)
            row_to_insert = []
        return result