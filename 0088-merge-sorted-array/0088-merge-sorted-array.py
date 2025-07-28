class Solution:
    def merge(
        self, nums_1: list[int], count_1: int, nums_2: list[int], count_2: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_1 = count_1 - 1
        index_2 = count_2 - 1
        total_index = count_1 + count_2 - 1

        while index_2 >= 0:
            if index_1 >= 0 and nums_1[index_1] > nums_2[index_2]:
                nums_1[total_index] = nums_1[index_1]
                index_1 -= 1
            else:
                nums_1[total_index] = nums_2[index_2]
                index_2 -= 1
            total_index -= 1
