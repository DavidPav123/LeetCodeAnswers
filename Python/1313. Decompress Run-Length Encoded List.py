from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        final_array = []
        for i in range(0,len(nums),2):
            final_array.extend([nums[i+1]] * nums[i])
        return final_array