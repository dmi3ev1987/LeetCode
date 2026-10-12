class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        set_num = set(str(n))
        result = 0
        for num in set_num:
            result += int(num) * int(str(n).count(num))
        return result
        