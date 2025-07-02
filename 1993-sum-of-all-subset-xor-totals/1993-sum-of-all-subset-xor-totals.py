from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        subsets = []
        total_xor_sum = 0
        for length in range(len(nums) + 1):
            for subset in combinations(nums, length):
                subsets.append(list(subset))

        for subset in subsets:
            xor = 0
            for num in subset:
                xor ^= num
            total_xor_sum += xor
        return total_xor_sum