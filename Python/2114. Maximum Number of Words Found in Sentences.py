from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for sentance in sentences:
            if len(sentance.split()) > max_len:
                max_len = len(sentance.split())
        return max_len
