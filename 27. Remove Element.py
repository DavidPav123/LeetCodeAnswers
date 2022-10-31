class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_copy = [i for i in nums if i != val]

        for num in range(len(nums_copy)):
             nums[num] = nums_copy[num]

        return len(nums_copy)

