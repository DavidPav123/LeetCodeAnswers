from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        answers = []
        for i in candies:
            if i + extraCandies >= max_candies:
                answers.append(True)
            else:
                answers.append(False)
        return answers
