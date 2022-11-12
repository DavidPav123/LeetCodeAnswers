from typing import List
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        maximum = 0
        minimum = 0
        averages = set()
        while len(nums) > 1:
            maximum = min(nums)
            nums.remove(maximum)
            minimum = max(nums)
            nums.remove(minimum)
            averages.add((minimum+maximum)/2)
        return len(averages)
