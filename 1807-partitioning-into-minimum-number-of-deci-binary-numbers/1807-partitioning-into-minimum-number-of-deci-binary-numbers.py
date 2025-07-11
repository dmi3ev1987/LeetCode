class Solution:
    def minPartitions(self, str_number: str) -> int:
        return max(int(number) for number in str_number)
