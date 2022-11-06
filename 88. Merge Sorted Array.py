class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0: return m
        else:
            for nums in enumerate(nums2):
                nums1[m + nums[0]] == nums2[1]
            nums1.sort()

