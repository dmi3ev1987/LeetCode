class Solution:
    def moveZeroes(self, numbers: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = numbers.count(0)
        for _ in range(zero_counter):
            numbers.remove(0)
            numbers.append(0)
        