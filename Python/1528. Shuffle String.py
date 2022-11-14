from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = list(s)
        final_arr = [0] * len(s)
        for i in range(len(indices)):
            final_arr[indices[i]] =  arr[i]
        return "".join(final_arr)