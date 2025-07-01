class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less_then_pivot = []
        equal_to_pivot = []
        greater_then_pivot = []
        for number in nums:
            if number < pivot:
                less_then_pivot.append(number)
            elif number == pivot:
                equal_to_pivot.append(number)
            else:
                greater_then_pivot.append(number)
        return less_then_pivot + equal_to_pivot + greater_then_pivot