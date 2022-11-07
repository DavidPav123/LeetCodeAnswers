class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = bin(n)[2:]
        for i in range(32-len(bin_str)):
            bin_str = "0" + bin_str
        return int(bin_str[::-1],2)