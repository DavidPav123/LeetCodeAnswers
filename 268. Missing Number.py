class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n not in nums:
            return n
        else:
            for i in range(n):
                if i not in nums:
                    return i
