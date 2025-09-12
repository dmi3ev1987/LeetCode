class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        result_count = 0
        numbers_sum = sum(nums)
        while numbers_sum > 0:
            if numbers_sum % k == 0:
                break
            numbers_sum -= 1
            result_count += 1
        return result_count
