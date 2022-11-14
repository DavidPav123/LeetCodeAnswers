from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            total_greater_than = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and i != j:
                    total_greater_than += 1
            new_nums.append(total_greater_than)
        return new_nums
