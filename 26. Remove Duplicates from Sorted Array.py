class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_copy = list(set(nums))
        nums_copy.sort()

        for num in range(len(nums_copy)):
             nums[num] = nums_copy[num]

        return len(nums_copy)