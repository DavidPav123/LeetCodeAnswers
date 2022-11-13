class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            remainder_stack = []
            decimal_number = n
            while decimal_number > 0:
                remainder = decimal_number % i
                remainder_stack.append(str(remainder))
                decimal_number = decimal_number // i
            str_num = "".join(remainder_stack[::-1])

            if str_num != str_num[::-1]:
                return False
        return True
