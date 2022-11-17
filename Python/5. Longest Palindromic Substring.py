from itertools import combinations


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        else:
            final_str = ""
            for i in range(len(s), 0, -1):
                test = [
                    com_str
                    for com_str in [
                        combo for combo in combinations(s, i) if combo == combo[::-1]
                    ]
                    if "".join(com_str) in s
                ]
                if len(test) > 0:
                    return "".join(test[0])
            return final_str
