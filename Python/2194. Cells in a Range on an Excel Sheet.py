from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        final_arr = []
        for char in range(ord(s[0]), ord(s[3]) + 1):
            for i in range(int(s[1]), int(s[4]) + 1):
                final_arr.append(chr(char) + str(i))
        return final_arr
