from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for num in encoded:
            decoded.append(num ^ decoded[-1])
        return decoded
