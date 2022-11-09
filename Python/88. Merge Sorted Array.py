class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return m
        else:
            for nums in nums2:
                nums1.append(nums)
                nums1.remove(0)
            nums1.sort()

