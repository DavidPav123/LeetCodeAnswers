class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x > -1:
            final = int(x_str[::-1])
            return final if final < (2**31) - 1 else 0
        else:
            final = int(x_str[1:][::-1]) * -1
            return final if final > (-(2 ** (31))) else 0
