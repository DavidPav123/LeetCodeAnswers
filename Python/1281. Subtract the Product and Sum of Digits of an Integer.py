class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        product = int(n[0])
        sum = 0
        for i in n:
            sum += int(i)
        for i in range(1, len(n)):
            product *= int(n[i])
        return product - sum
