from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        if total_len % 2:
            for i in range(int((total_len - 1) / 2)):
                if not nums1:
                    nums2.pop(0)
                elif not nums2:
                    nums1.pop(0)
                else:
                    if nums1[0] > nums2[0]:
                        nums2.pop(0)
                    else:
                        nums1.pop(0)
            if len(nums2) == 0:
                return nums1[0]
            elif len(nums1) == 0:
                return nums2[0]
            else:
                if nums1[0] < nums2[0]:
                    return nums1[0]
                else:
                    return nums2[0]
        else:
            for i in range(total_len - 2):
                if not nums1:
                    if i % 2:
                        nums2.pop(0)
                    else:
                        nums2.pop()
                elif not nums2:
                    if i % 2:
                        nums1.pop(0)
                    else:
                        nums1.pop()
                else:
                    if i % 2:
                        if nums1[0] > nums2[0]:
                            nums2.pop(0)
                        else:
                            nums1.pop(0)
                    else:
                        if nums1[-1] > nums2[-1]:
                            nums1.pop()
                        else:
                            nums2.pop()
            if len(nums1) == 0:
                return (nums2[0] + nums2[1]) / 2
            elif len(nums2) == 0:
                return (nums1[0] + nums1[1]) / 2
            else:
                return (nums1[0] + nums2[0]) / 2
