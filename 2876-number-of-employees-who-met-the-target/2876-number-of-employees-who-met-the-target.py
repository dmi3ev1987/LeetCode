class Solution:
    def numberOfEmployeesWhoMetTarget(
        self, hours: list[int], target: int
    ) -> int:
        return sum(number >= target for number in hours)
