class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """List Comprehension Syntax.

        The general structure is:
            [expression for outer_loop for inner_loop ... if condition]
        """
        return [
            number
            for sublist in (
                [nums[index], nums[index + n]] for index in range(n)
            )
            for number in sublist
        ]
