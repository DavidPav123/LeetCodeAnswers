from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        final_array = []
        for i in range(len(nums)):
            final_array.insert(index[i], nums[i])
        return final_array
