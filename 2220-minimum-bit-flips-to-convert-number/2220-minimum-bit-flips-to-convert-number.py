class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin, goal_bin = bin(start)[2:], bin(goal)[2:]
        max_len = max(len(start_bin), len(goal_bin))
        if max_len == len(start_bin):
            goal_bin = goal_bin.zfill(max_len)
        else:
            start_bin = start_bin.zfill(max_len)
        return sum(a != b for a, b in zip(start_bin, goal_bin))
