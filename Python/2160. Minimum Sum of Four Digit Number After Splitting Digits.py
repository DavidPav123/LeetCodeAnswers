class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        return int("".join(str(num[0] + num[3]))) + int("".join(str(num[1] + num[2])))
