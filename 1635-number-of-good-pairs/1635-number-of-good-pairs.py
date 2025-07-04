class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = 0
        while nums:
            count += nums.count(nums.pop(0))
        return count